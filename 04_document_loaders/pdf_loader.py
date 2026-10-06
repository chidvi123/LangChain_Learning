from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample_company_policy.pdf')

documents = loader.load()


print("Number of pages:", len(documents))

print("\nFirst page content:")
print(documents[0].page_content)

print("\nFirst page metadata:")
print(documents[0].metadata)