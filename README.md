
📄 RAG with LangChain and Gemini - AI PDF Assistant

A Streamlit-based AI assistant that allows users to upload a PDF document and ask context-based questions about its content. This app uses LangChain, FAISS, HuggingFace embeddings, and Google Gemini to retrieve and generate accurate answers.

🚀 Features
- 📄 Upload any PDF file and extract text
- 🔍 Split the PDF into manageable chunks using LangChain
- 🧠 Store and search chunks using FAISS Vector DB
- 🤖 Generate answers with Google Gemini (Gemini 2.0 Flash)
- 💬 Simple and intuitive Streamlit interface

🛠️ Tech Stack
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers (all-MiniLM-L6-v2)
- Google Generative AI (Gemini)

🔐 Setup and Installation

1. Clone the repository
   git clone https://github.com/niranjanq/rag.AI.git
   cd ai-doc-assistant

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  (on Windows: venv\Scripts\activate)

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   Create a .env file in the root directory and add your Gemini API key:
   GOOGLE-API-KEY=your_gemini_api_key

▶️ Run the App
   streamlit run app.py

   Open the app in your browser, upload a PDF, and start asking questions!

📂 Project Structure
.
├── app.py              # Main Streamlit app
├── .env                # Environment variables (not committed)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies

⚠️ Limitations
- Only supports text-based PDFs
- Works best with concise or well-structured documents
- Gemini output may slightly vary due to the generative nature of LLMs

🙌 Acknowledgements
- Google Generative AI
- HuggingFace (MiniLM embeddings)
- LangChain for RAG pipeline
- Streamlit for rapid UI development

📬 Contact
For questions or suggestions, contact: npniranjan2001@gmail.com
Do visit on: https://askmydocsai.streamlit.app/
