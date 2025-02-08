from perplexity_api import query_perplexity
print(query_perplexity([
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": "I go to the dark room"
            }
        ]))
