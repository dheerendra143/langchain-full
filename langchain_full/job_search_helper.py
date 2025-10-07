

import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import llm.config.job_search_helper as chat



# with open("langchain_full/job_listings.txt", 'rb') as f:
#     raw_data = f.read()
# result = chardet.detect(raw_data)
# print(result)
# encoding = result['encoding']
# print(f"Detected encoding: {encoding}")

document = TextLoader("langchain_full/data/job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)

chucks = text_splitter.split_documents(document)

db = Chroma.from_documents(chucks, chat.llm)



st.title("Speech Generator")

text = st.text_input(
    label="Enter question1",
)
if text:
    embedding_vector = chat.llm.embed_query(text)
    docs = db.similarity_search_by_vector(embedding_vector)
    for doc in docs:
        print(doc)
        st.write(doc.page_content)
