from langchain_community.retrievers import BM25Retriever
from .chunks import chunk

retriver=BM25Retriever.from_documents(
    chunk,
    k=3
)

query=input("ask any question")

results=retriver.invoke(query)

# content="\n\n".join(
#     result.page_content for result in results
# )

for i, results in enumerate(results,1):
    print(f"resutlt{i}")
    print("content",results.page_content)
    print("sourve",results.metadata.get("source"))

# print(content)
