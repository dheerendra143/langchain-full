

import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_croma import Chroma
from langchain_ollama import OllamaEmbeddings

llm = OllamaEmbeddings(model="llama3.2")


document = TextLoader("langchain_full/data/product-data.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunks = text_splitter.split_documents(document)
db = Chroma.from_documents(chunks, llm)

st.title("Speech Generator")

text = st.text_input(
    label="Enter question1",
)
if text:
    embedding_vector = llm.embed_query(text)
    docs = db.similarity_search_by_vector(embedding_vector)
    for doc in docs:
        print(doc)
        st.write(doc.page_content)
