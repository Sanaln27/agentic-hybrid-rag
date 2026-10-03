from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
"""
    You are a professional llm helping the rag system
    -you take chunks(use the chunks efficently) and generate the answer
    -Make sure the answer is precise and shoert
    -dont miss any key points or values in term of the making things shiet 
-
    


Context:
{context}

Question:
{question}

Answer:
"""
)


