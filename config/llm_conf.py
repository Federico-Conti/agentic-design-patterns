from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_KEY   


try:

    llm = AzureChatOpenAI(
        azure_deployment="ict-agent_gpt4omini",  
        api_version="2024-12-01-preview", 
        temperature=0.3,
        max_tokens=100,
        timeout=None,
        max_retries=2,
    )
    print(f"Language model initialized")
    
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None



# messages = [
#     SystemMessage(content="You're a helpful assistant"),
#     HumanMessage(
#         content="What happens when an unstoppable force meets an immovable object?"
#     ),
# ]

# ai_msg = llm.invoke(messages)
# print(ai_msg.content)