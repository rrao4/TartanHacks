from perplexity_api import query_perplexity

def start_game():
    # Initialize game state and first story beat
    game_state = {
        'beat_count': 0,
        'history': [],
        'theme': None  # To be set after querying Perplexity
    }
    return game_state

def process_turn(state, user_input):
    prompt = f"Game state: {state}\nUser input: {user_input}\nContinue the story:"
    ai_response = query_perplexity(prompt)

    # Update the game state (modify this logic as needed)
    updated_state = {**state, "last_input": user_input, "last_response": ai_response}

    return updated_state, ai_response
