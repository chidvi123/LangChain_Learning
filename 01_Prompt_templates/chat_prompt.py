from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system","you are an AI tutor who explains concepts simply"),
    ('human','Explain {topic} using {context}')
])

result = prompt.invoke({
    "topic": "RAG",
    "context": "retrieving relevant information before generating an answer"
})

print(result)