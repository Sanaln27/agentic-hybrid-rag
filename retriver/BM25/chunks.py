from retriver.Dense.dc_loader import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter

def data_base():
    documents=load_documents("data1")

#do chunking
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=1000
    )

    chunk=splitter.split_documents(documents)

    return chunk

chunk=data_base()

print(len(chunk))
print(chunk[0])