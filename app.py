import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

from langchain_core.documents import Document

from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS




# API Configuration

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
gemini_model=genai.GenerativeModel("gemini-2.0-flash")


# Cache the HF embeddings to avoid slow reload of the embeddings

@st.cache_resource(show_spinner="Loading embeddings...")

# Activate the embeddings
def embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

embedding_model=embeddings()

# UI 
st.header("RAG with LangChain and Gemini")
st.subheader("Your personal AI doc assistant")


upload_file=st.file_uploader(label="Upload a PDF file", type=["pdf"])



if upload_file:
    raw_text=""
    pdf=PdfReader(upload_file)
    for i,page in enumerate(pdf.pages):
        text=page.extract_text()
        if text:
            raw_text+=text
    # st.write("PDF file loaded successfully")
    
    if raw_text.strip():
        document=Document(page_content=raw_text)
        # Using CharacterTextSplitter to split the text into chunks and pass it into the model
        splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks=splitter.split_documents([document])
        
        # Source the chunks into faiss vectorDB
        chunk_pieces=[chunk.page_content for chunk in chunks]
        vectordb=FAISS.from_texts(chunk_pieces, embedding_model)
        retriever=vectordb.as_retriever() # Retrieve the vectors
        st.success("PDF file split into chunks and stored in vectorDB. Ask your question!!!")
        # User QnA
        user_input=st.text_input(label="Ask your question about the PDF file")
        if user_input:
            with st.chat_message("user"):
                st.write(user_input)
            with st.spinner("Thinking..."):
                relevant_doc=retriever.get_relevant_documents(user_input)
                context="\n\n".join([doc.page_content for doc in relevant_doc])
                prompt=f'''You are expert assisatnt. Use the context below to answer the query. If Unsure or information not available 
                in the doc,pass the message- "Information is not available. Look into other sources"
                context: {context}
                query: {user_input}
                Answer:
                '''
                response=gemini_model.generate_content(prompt)
                st.markdown("Answer:")
                st.write(response.text)
    else:
        st.warning('''No text could be extracted from the PDF file. Please check the file and try again.''')