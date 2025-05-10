📄 RAG with LangChain and Gemini - AI PDF Assistant
A Streamlit-based AI assistant that allows users to upload a PDF document and ask context-based questions about its content. The application uses LangChain, FAISS, HuggingFace embeddings, and Google Gemini to retrieve and generate accurate answers.

🚀 Features
📄 Upload any PDF file and extract text.

🔍 Split the PDF into manageable chunks using LangChain.

🧠 Store and search chunks using FAISS Vector DB.

🤖 Use Google Gemini (Gemini 2.0 Flash) to generate answers from the most relevant context.

💬 Simple and intuitive Streamlit interface.

🛠️ Tech Stack
Streamlit

LangChain

FAISS

HuggingFace Transformers

Google Generative AI (Gemini)

🔐 Setup and Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/ai-doc-assistant.git
cd ai-doc-assistant
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your environment variables:

Create a .env file in the root directory and add your Gemini API key:

ini
Copy
Edit
GOOGLE-API-KEY=your_gemini_api_key
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Open the app in your browser, upload a PDF, and start asking questions!

📂 Project Structure
bash
Copy
Edit
.
├── app.py              # Main Streamlit app
├── .env                # Environment variables (not committed)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
⚠️ Limitations
Only supports text-based PDFs.

Works best with concise documents or well-structured reports.

Gemini output may vary slightly due to generative nature.

🙌 Acknowledgements
Google Generative AI

HuggingFace for MiniLM embeddings

LangChain for streamlined RAG flow

Streamlit for easy UI development

📬 Contact
For questions or suggestions, reach out at [your-email@example.com]