from langchain_community.retrievers import BM25Retriever
from .chunks import chunk

retriver=BM25Retriever.from_documents(
    chunk,
    k=3
)

results = retriver.invoke("What programming skills does Nabneet have?")

for result in results:
    print(result.page_content)
    print(result.metadata)
    print("----------------")