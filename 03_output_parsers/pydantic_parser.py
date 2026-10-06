from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class Topic(BaseModel):
    name: str
    difficulty: str
    description: str


parser = PydanticOutputParser(pydantic_object=Topic)

output = """
{
    "name": "RAG",
    "difficulty": "Beginner",
    "description": "Retrieval-Augmented Generation combines retrieval with LLM generation."
}
"""

result = parser.parse(output)

print(result)
print(type(result))