import base64
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = "ict-chatiit_gpt4o"

subscription_key = os.getenv("AZURE_OPENAI_KEY")
api_version = "2025-04-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
    default_headers={"x-ms-oai-image-generation-deployment":"ict-chatiit_gptimage1", "api_version":"preview"}
)

response = client.responses.create(
    model=deployment,
    # input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    input="The quick brown fox jumps over the lazy dog",

    tools=[{"type": "image_generation"}],
)


image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
else:
    print(response.output_text)  # Print the text response if no image was generated