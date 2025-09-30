

import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.main_ollama as chat
import llm.propts.speechGenerator as code_prompt


prompt_template1 = PromptTemplate(
    input_variables=["topic"],
    template=code_prompt.template1
)

prompt_template2 = PromptTemplate(
    input_variables=["title"],
    template=code_prompt.template2
)


first_chain = prompt_template1 | chat.llm
second_chain = prompt_template2 | chat.llm
final_chain = first_chain | second_chain


st.title("Speech Generator")

topic = st.text_input(
    label="Enter topic",
    )


if topic:
    resource = final_chain.stream({"topic": topic})
    st.write_stream(resource)