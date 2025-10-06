

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.main_ollama as chat
import llm.prompts.speechGenerator as code_prompt
import  data as data

document = TextLoader("data/product-data.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(document)
vector_store = Chroma.from_document(chunks)
retriever = vector_store.as_retriver()


prompt_template = ChatPromptTemplate.from_message(
[
    ("system", """You are an assistance for answering questions.
    use the provided context to response. If the answer isn't clear, acknowledge that
    you dont know.
    Limit your response to three concise sentences.
    {context}

    """),
    ("human", "{input}")
])





qa_chain = create_stuff_documents_chain(llm, prompt_template )
req_chain = create_retrival_chain(retriever, qa_chain )

# first_chain = prompt_template1 | chat.llm
# second_chain = prompt_template2 | chat.llm
# final_chain = first_chain | second_chain


st.title("Speech Generator")

question = st.text_input(
    label="Enter question",
    )


if question:
    resource = final_chain.stream({"input": question})
    st.write_stream(resource['answer'])