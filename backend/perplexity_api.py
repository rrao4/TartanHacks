import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
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
        "model": "sonar",  # Ensure this is a supported model
        "messages": history,  # Send the full chat history
        "max_tokens": 10  # Adjust length for better responses
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise error if response is not 2xx

        # Extract AI response from "choices"
        response_data = response.json()
        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response found.")
    except requests.exceptions.RequestException as e:
        return f"API Request Failed: {e}"
