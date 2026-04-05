from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from app.config import *

# Azure OpenAI
llm = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# Azure AI Search
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)

def retrieve_context(query):
    results = search_client.search(query, top=3)
    return [doc["content"] for doc in results]

def generate_response(prompt):
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content