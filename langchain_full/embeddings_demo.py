

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
import llm.config.openai_embedding as chat
import numpy as np

st.title("Speech Generator")

question = st.text_input(
    label="Enter question1",
)

question2 = st.text_input(
    label="Enter question2",
)



if question and question2:
    resource = chat.llm.embed_query(question)
    resource2 = chat.llm.embed_query(question2)

    similarity_score = np.dot(resource, resource2)

    print(similarity_score * 100, '%')
    # st.write_stream(resource)