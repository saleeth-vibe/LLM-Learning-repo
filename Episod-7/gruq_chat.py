from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("groq_api_key")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key
)

print(llm.invoke("What should i do after finishing my work?").content)
