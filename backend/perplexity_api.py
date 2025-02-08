import requests
import os
from dotenv import load_dotenv

load_dotenv()
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def query_perplexity(history):
    """Sends the conversation history to Perplexity AI and returns the next story beat."""
    if not PERPLEXITY_API_KEY:
        return "Error: Missing Perplexity API Key."

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar", 
        "messages": history, 
        "max_tokens": 250
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status() 

        # get AI response and return
        response_data = response.json()
        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response found.")
    except requests.exceptions.RequestException as e:
        return f"API Request Failed: {e}"
