from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ('system','You are a helpful AI tutor'),
    ('human','Explain {topic} in simple words')
])

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

parser=StrOutputParser() # takes the string that llm generates and returns as a normal python 

chain = prompt | llm | parser

result = chain.invoke({
    'topic':'RAG'
})

print(result)