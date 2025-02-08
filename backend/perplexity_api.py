import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def query_perplexity(prompt: str):
    """Sends a request to Perplexity AI and returns the generated response."""
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Correcting API request format
    data = {
        "model": "sonar",  # Check Perplexity's documentation for supported models
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": prompt  # Correctly inserting user's input
            }
        ],
        "max_tokens": 1  # Controls response length
    }
    print(url)
    print(PERPLEXITY_API_KEY)
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise error if response is not 2xx

        # Extract AI response from "choices"
        response_data = response.json() 
        content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response found.")
        #print("AI Response:", content)
        return content

        # response_data = response.json()
        # return response_data.get("choices", [{}])[0].get("message", {}).get("content", "Error: No response.")
    except requests.exceptions.RequestException as e:
        return f"API Request Failed: {e}"
