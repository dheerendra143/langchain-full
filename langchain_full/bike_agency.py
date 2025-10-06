from email.policy import default

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.main_ollama as chat
import llm.prompts.bikePrompt as code_prompt


prompt_template = PromptTemplate(
    input_variables=["city", "month", "language", "company"],
    template=code_prompt.template
)

st.title("Bike Guide assistance")

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


company = st.text_input(
    label="Enter company",
    placeholder="Enter company"
    )


if city and month and language and company:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    input_prompt = prompt_template.format(city=city, month=month, language=language, company=company)
    resource = chat.llm.stream(input_prompt)
    # with st.container(height=300):  # Adjust height as needed
    st.write_stream(resource)