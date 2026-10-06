from langchain_core.runnables import RunnableLambda


# RunnableLambda - simply wraps a normal Python function so that LangChain can treat it as a Runnable component.
double = RunnableLambda(lambda x: x*2)

add_ten= RunnableLambda(lambda x : x+10)

chain = double | add_ten

result = chain.invoke(5)

print(result)