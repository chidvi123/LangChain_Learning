from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("sample_company_policy.docx")
documents = loader.load()

for doc in documents:
    print(doc.page_content)
    print(doc.metadata)