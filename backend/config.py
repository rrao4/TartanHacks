import os

class Config:
    DEBUG = os.getenv('DEBUG', True)
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY', 'your-api-key-here')
