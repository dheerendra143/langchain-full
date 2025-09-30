import streamlit as st
import llm.config.basic as chat


st.title("Chat with Ollama")
st.subheader('This is a small application')
query = st.text_input(label="Enter your query", placeholder="Write your query here")
if query:
    # resource = chat.chain.invoke(query)
    # st.write(resource.content)
    resource = chat.llm.stream(query)
    st.write_stream(resource)