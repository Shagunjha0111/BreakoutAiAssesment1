AI Agent Project
An intelligent agent designed to process structured data from CSV files or Google Sheets, perform web searches based on user-defined queries, extract information using a language model (LLM), and present the results in an intuitive dashboard.

📜 Project Overview
This AI agent leverages cutting-edge AI technologies to streamline data analysis and information retrieval. It automates:

Data ingestion from CSV files or Google Sheets.
Web searches based on user-defined queries.
Information extraction from specific data columns using an LLM.
Dashboard presentation for seamless user interaction.
The project is ideal for handling large datasets and performing research tasks with precision and speed.

🛠️ Setup Instructions
Prerequisites
Python 3.8 or later.
pip for package installation.
Streamlit for the dashboard.
API keys for the following:
SERPAPI: For web search.
Hugging Face: For LLM-based information extraction.
Google Cloud: For accessing Google Sheets.
Clone the Repository
bash
Copy code
git clone https://github.com/Shagunjha0111/ai-agent-project.git
cd ai-agent-project
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the root directory and add the following:
env
Copy code
SERPAPI_API_KEY=your_serpapi_key
GOOGLE_CREDENTIALS_PATH=path_to_google_credentials.json
HUGGINGFACE_API_KEY=your_huggingface_key
OPENAI_API_KEY=your_openai_key
▶️ Usage Guide
Run the Streamlit App
bash
Copy code
C:\Python312\python.exe -m streamlit run "file_path.py"
Upload Your Data
Use the app's interface to upload a CSV file or connect to a Google Sheet.
Define Queries
Enter your custom queries to perform web searches on the uploaded data.
Extract Information
Specify the column for extraction. The AI model processes it to fetch relevant details.
View Results
Check the processed data and insights in the interactive dashboard.
🧰 Key Features
Automated Data Handling: Processes data from multiple sources with ease.
AI-Powered Search: Leverages LLMs to extract meaningful insights.
Customizable Queries: Tailor the search and extraction process as per your needs.
User-Friendly Dashboard: Intuitive visualization for quick analysis and decision-making.
🔗 Third-Party APIs & Tools
SERPAPI: Facilitates seamless web search.
Hugging Face Transformers: Powers the LLM for information extraction.
Google Cloud API: Enables integration with Google Sheets.
Streamlit: Provides an interactive dashboard interface.
📧 Contact
For questions or collaboration opportunities, reach out at GitHub Profile.








