import os
import mysql.connector
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage
from tools.tools import mysql_tool,rag_tool
from model.config import llm
from memory.conversation import histroy,add_msg

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)


tools=[
    mysql_tool,
    rag_tool
    ]

agent=create_agent(
    model=llm,
    tools=tools
)

while True:
    question=input("\nmeee:\n")
    if question.lower()=="exit":
        print("boyee boyeee")
        break 
    add_msg(
        role="user",
        content=question
    )


    response = agent.invoke({
        "messages":histroy()
    })

    answer=response["messages"][-1].content

    add_msg(
        role="assistant",
        content=answer
    )

    print(answer)