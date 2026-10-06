from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

output = "RAG, LangChain, Embeddings, Vector Database"

result = parser.parse(output)

print(result)
print(type(result))