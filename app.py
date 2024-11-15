import os
import pandas as pd
import streamlit as st
import requests
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from concurrent.futures import ThreadPoolExecutor
import re
from time import sleep

# Load environment variables
load_dotenv()

# API keys and paths
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

# Regular expression patterns for fallback extraction
PHONE_PATTERN = r"\+?\(?\d{1,4}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Fetch search results from SerpAPI
def fetch_search_results(query):
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("organic_results", [])
    else:
        return None

# Extract information using Hugging Face API
def extract_information_with_llm(text, query):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": f"Query: {query} Context: {text}"}
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0].get("summary_text", "No summary extracted")
    return None

# Fallback extraction with regex
def extract_fallback(text, extract_phone=False, extract_email=False):
    extracted = {"phones": [], "emails": []}
    if extract_phone:
        extracted["phones"] = re.findall(PHONE_PATTERN, text)
    if extract_email:
        extracted["emails"] = re.findall(EMAIL_PATTERN, text)
    return extracted

# Process a single entity
def process_entity(entity, query_template, extract_phone=False, extract_email=False):
    query = query_template.format(entity=entity)
    search_results = fetch_search_results(query)
    if search_results:
        search_results_text = " ".join(result.get('snippet', '') for result in search_results)
        llm_output = extract_information_with_llm(search_results_text, query)
        
        # Conditionally extract phones and emails based on user choice
        fallback = extract_fallback(search_results_text, extract_phone, extract_email)
        
        return {
            "LLM Output": llm_output,
            "Fallback Phones": fallback["phones"],
            "Fallback Emails": fallback["emails"]
        }
    return {"LLM Output": "No results", "Fallback Phones": [], "Fallback Emails": []}

# Google Sheets Authentication
def authenticate_google_sheets(json_key_file):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_key_file, scope)
    client = gspread.authorize(creds)
    return client

# Fetch Google Sheets data
def get_google_sheet_data(sheet_url):
    try:
        client = authenticate_google_sheets(GOOGLE_CREDENTIALS_PATH)
        sheet = client.open_by_url(sheet_url)
        worksheet = sheet.get_worksheet(0)
        data = pd.DataFrame(worksheet.get_all_records())
        return data
    except Exception as e:
        st.error(f"Error reading Google Sheet: {e}")
        return None

# Streamlit UI
st.title("AI Agent for Dynamic Information Extraction")
st.markdown("Upload a CSV file or connect a Google Sheet to extract custom information dynamically.")

# Handle file upload or Google Sheet URL
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
google_sheet_url = st.text_input("Enter Google Sheet URL:")

# Fetch data based on input
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of your data:", df.head())
elif google_sheet_url:
    df = get_google_sheet_data(google_sheet_url)
    if df is not None:
        st.write("Google Sheet Data Preview:", df.head())
    else:
        st.error("Failed to load Google Sheet data.")

# Process the data for extraction
if df is not None:
    column_name = st.text_input("Enter the column name to extract from:", value="Name")
    if column_name not in df.columns:
        st.error(f"The uploaded file does not contain a '{column_name}' column.")
    else:
        entities = df[column_name].tolist()
        
        # User-defined query template
        query_template = st.text_input(
            "Enter your query template (use {entity} as placeholder):",
            value="Find the contact details of {entity}"
        )
        
        # Check for entity placeholder in query template
        if "{entity}" not in query_template:
            st.error("Query template must include '{entity}' as a placeholder.")
        else:
            # Options to extract phone numbers and emails conditionally
            extract_phone = st.checkbox("Extract phone numbers", value=False)
            extract_email = st.checkbox("Extract emails", value=False)

            # Process entities in parallel
            progress = st.progress(0)
            results = []
            with ThreadPoolExecutor() as executor:
                for i, result in enumerate(executor.map(lambda e: process_entity(e, query_template, extract_phone, extract_email), entities)):
                    results.append(result)
                    progress.progress((i + 1) / len(entities))
            
            # Update DataFrame with results
            df["LLM Output"] = [r["LLM Output"] for r in results]
            df["Fallback Phones"] = [r["Fallback Phones"] for r in results]
            df["Fallback Emails"] = [r["Fallback Emails"] for r in results]
            
            # Display results in table
            st.write("Extracted Data:", df)

            # Options to download the results
            if st.button("Download as CSV"):
                download_link = df.to_csv(index=False)
                st.download_button(label="Download CSV", data=download_link, file_name="extracted_data.csv")

            # Option to update Google Sheets with results
            if st.button("Update Google Sheet"):
                try:
                    client = authenticate_google_sheets(GOOGLE_CREDENTIALS_PATH)
                    sheet = client.open_by_url(google_sheet_url)
                    worksheet = sheet.get_worksheet(0)
                    
                    # Convert DataFrame rows into proper format for appending
                    for i, row in df.iterrows():
                        # Convert each row into a list of strings before appending
                        row_data = [str(item) for item in row.tolist()]
                        worksheet.append_row(row_data)
                    st.success("Google Sheet updated successfully.")
                except Exception as e:
                    st.error(f"Error updating Google Sheet: {e}")


            



