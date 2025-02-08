import requests
from config import Config

def query_perplexity(prompt):
    # Construct the API request payload
    headers = {
        'Authorization': f"Bearer {Config.PERPLEXITY_API_KEY}",
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt
    }
    # Replace with the actual Perplexity API endpoint
    response = requests.post('https://api.perplexity.ai/v1/endpoint', json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Error handling can be enhanced here
        return {'error': 'API request failed'}
