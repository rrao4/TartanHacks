import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def query_perplexity(prompt):
    if not PERPLEXITY_API_KEY:
        return "Error: Missing Perplexity API Key"

    url = "https://api.perplexity.ai/generate"  # Replace with the actual API URL
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 200
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json().get("text", "Error: No response from Perplexity")
