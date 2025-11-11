
from langchain_community.chat_models import ChatOllama
from langchain import hub
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
import streamlit as st
# from langchain_community.tools import duckduckgo_search

# llm = ChatOllama(model="gemma:2b")
llm = ChatOllama(model="llama3.2")

prompt = hub.pull("hwchase17/react")


tools = load_tools([ "ddg-search"])

# # 2. Define Tools (Example: a simple search tool)
# def search_tool_func(query: str) -> str:
#     # Implement your search logic here
#     return f"Result for '{query}': Example search result."

# search_tool = Tool(
#     name="Search",
#     func=search_tool_func,
#     description="Useful for searching information on a given topic."
# )
# tools = [search_tool]

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

st.title("Agent with Ollama")
task = st.text_input(label="Enter your task", placeholder="Describe your task here")

if task:
    response = agent_executor.invoke({"input": task})
    st.write(response["output"])
