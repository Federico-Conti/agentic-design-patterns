import json
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = "ict-chatiit_gpt4o"

subscription_key = os.getenv("AZURE_OPENAI_KEY")
api_version = "2025-04-01-preview"

response_id = os.getenv("AZURE_OPENAI_RESPONSE_ID")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# STEP 1: Create a conversation

response = client.responses.create(
    model=deployment,
    input="Mi chiamo Federico e sono uno studente di ingegneria informatica a Torino",
)

print(response)

# STEP 2: Retrieve the conversation from ID 
response_retrieved = client.responses.retrieve(response_id)
print(response_retrieved)


