from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings

llm = OllamaEmbeddings(model="llama3.2")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "{prompt}"),
#     ("user", "{input}")
# ])
# output_parser = StrOutputParser()

chain = llm