from email.policy import default

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.code_agent_config as chat
import llm.propts.prompTemplate as code_promp


prompt_template = PromptTemplate(
    input_variables=["country", "on_of_paras", "language"],
    template=code_promp.template
)

st.title("Cuisine assistance")
country = st.text_input(
    label="Enter country name",
    placeholder="Enter country name"
    )

no_of_paras = st.number_input(
    label="Enter number of paras",
    min_value=1,
    max_value=15
)

language = st.text_input(
    label="Enter language",
    placeholder="Enter language"
    )


if language:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(prompt_template.format(country=country, no_of_paras=no_of_paras, language=language))
    # with st.container(height=300):  # Adjust height as needed
    st.write_stream(resource)