

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
import llm.config.openai_embedding as chat


st.title("Speech Generator")

question = st.text_input(
    label="Enter question",
)


if question:
    resource = chat.llm.embed_query(question)
    st.write_stream(resource)