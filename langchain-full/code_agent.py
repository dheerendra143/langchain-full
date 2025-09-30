import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.code_agent_config as chat
import llm.propts.codeAgentPrompt as code_promp


st.title("Technical assistance")
st.subheader('This is a small application which help to solve the technical issue for the developer')
query = st.text_input(
    label="Enter your technical query",
    placeholder="Write your query here",
    )

prompt_template = PromptTemplate(
    input_variables=["code"],
    template=code_promp.template
)

if query:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(prompt_template.format(code=query))
    with st.container(height=300):  # Adjust height as needed
        st.write_stream(resource)