Loom video link 
https://www.loom.com/share/93dfb492f2054d8f8396db62a205cfb7?sid=d6838f8b-061b-40e0-acd2-df6b4d9e3749

AI Agent Project
An intelligent agent designed to process structured data from CSV files or Google Sheets, perform web searches based on user-defined queries, extract information using a language model (LLM), and present the results in an intuitive dashboard.

📜 Project Overview
This AI agent leverages cutting-edge AI technologies to streamline data analysis and information retrieval. It automates the following tasks:

Data ingestion: Supports CSV files and Google Sheets as input.
Web searches: Executes searches based on user-defined queries.
Information extraction: Utilizes LLMs to extract relevant data from specified columns.
Dashboard presentation: Displays results and insights in an interactive and user-friendly interface.
This project is designed for handling large datasets and research tasks with precision and efficiency.

🛠️ Setup Instructions
Prerequisites
Ensure you have the following installed:

1.Python: Version 3.8 or later.
2.pip: For managing Python packages.
3.Streamlit: For creating the dashboard interface.

You will also need API keys for:
1.SERPAPI: For web search functionality.
2.Hugging Face: For LLM-based processing.
3.Google Cloud: For accessing Google Sheets.

Clone the Repository
Copy code
git clone https://github.com/Shagunjha0111/ai-agent-project.git
cd ai-agent-project


Install Dependencies
Copy code
pip install -r requirements.txt

Set Up Environment Variables
Create a .env file in the root directory with the following content:
Copy code
SERPAPI_API_KEY=your_serpapi_key
GOOGLE_CREDENTIALS_PATH=path_to_google_credentials.json
HUGGINGFACE_API_KEY=your_huggingface_key
OPENAI_API_KEY=your_openai_key

▶️ Usage Guide
Run the Streamlit App
Execute the following command to launch the app:

Copy code
C:\Python312\python.exe -m streamlit run "file_path.py"

Steps to Use the App
1.Upload Your Data
Upload a CSV file or connect to a Google Sheet via the app interface.
2.Define Queries
Enter your custom queries to perform web searches related to the uploaded data.
3.Extract Information
Specify the column for data extraction. The AI model will process it and extract meaningful information.
4.View Results
Check the processed data and insights in the interactive dashboard.


🧰 Key Features
1.Automated Data Handling: Seamlessly processes data from various sources.
2.AI-Powered Search: Leverages advanced LLMs to extract meaningful insights.
3.Customizable Queries: Enables tailored search and extraction processes.
4.User-Friendly Dashboard: Provides intuitive visualization for quick analysis.

🔗 Third-Party APIs & Tools
1.SERPAPI: Handles efficient web searches.
2.Hugging Face Transformers: Powers LLM-based information extraction.
3.Google Cloud API: Enables Google Sheets integration.
4.Streamlit: Builds the interactive dashboard.

📧 Contact
For questions or collaboration opportunities, please visit my GitHub Profile.






