import os
import openai
from openai import AzureOpenAI
from langchain_openai import AzureOpenAI, AzureChatOpenAI


from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("OPENAI_API_VERSION")
deployment_name = os.getenv("DEPLOYMENT_NAME")
model_name = os.getenv("MODEL_NAME")

print(endpoint)


llm = AzureChatOpenAI(
    deployment_name=deployment_name,
    openai_api_version=api_version,
)


llm.invoke("Tell me a joke")


# print("Creating client")
# client = AzureOpenAI(
#     api_key=api_key,
#     api_version="2024-02-01",
#     azure_endpoint=endpoint,
# )

# # Send a completion call to generate an answer
# print("Sending a test completion job")
# start_phrase = "Write a tagline for an ice cream shop. "
# response = client.completions.create(
#     model=deployment_name,
#     prompt=start_phrase,
#     max_tokens=10,
# )
# print(start_phrase + response.choices[0].text)
