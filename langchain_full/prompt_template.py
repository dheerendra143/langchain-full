import streamlit as st
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

import llm.config.code_agent_config as chat
import llm.propts.codeAgentPrompt as code_promp


st.title("Cuisine assistance")
query = st.text_input(
    label="Enter country name",
    placeholder="Enter country name",
    )

prompt_template = PromptTemplate(
    input_variables=["country"],
    template=code_promp.template
)

if query:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(prompt_template.format(country=query))
    with st.container(height=300):  # Adjust height as needed
        st.write_stream(resource)