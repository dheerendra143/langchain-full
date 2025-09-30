from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="gemma:2b")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful AI assistant."),
#     ("user", "{input}")
# ])
# output_parser = StrOutputParser()

chain = llm