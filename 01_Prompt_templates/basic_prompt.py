from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate.from_template(
    "Explain {topic} using  {context}"
)

result = prompt.invoke({
    "topic":"RAG",
    "context":"retrived information from a document"
})

print(result)