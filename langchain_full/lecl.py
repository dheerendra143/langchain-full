from email.policy import default

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.main_ollama as chat
import llm.propts.travelGuide as code_prompt


prompt_template = PromptTemplate(
    input_variables=["city", "month", "language", "budget"],
    template=code_prompt.template
)

st.title("Travel Guide assistance")

city = st.text_input(
    label="Enter city",
    placeholder="Enter city"
    )

month = st.text_input(
    label="Enter month",
    placeholder="Enter month"
    )

language = st.text_input(
    label="Enter language",
    placeholder="Enter language"
    )

budget = st.selectbox("Travel Budget", ["low", "medium", "high"])

llm_chat = prompt_template | chat.llm

if city and month and language and budget:
    resource = llm_chat.stream({
        "city": city,
        "month": month,
        "language": language,
        "budget": budget,
    })
    st.write_stream(resource)