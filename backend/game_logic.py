def start_game():
    # Initialize game state and first story beat
    game_state = {
        'beat_count': 0,
        'history': [],
        'theme': None  # To be set after querying Perplexity
    }
    return game_state

def process_turn(state, user_input):
    # Update the game state with user input
    state['history'].append(user_input)
    state['beat_count'] += 1

    # Here, integrate the call to Perplexity API to generate the next story beat.
    story_beat = f"Story beat {state['beat_count']}: Placeholder narrative response."

    # End the story if 10 beats have been reached.
    if state['beat_count'] >= 10:
        story_beat += " The story ends here."
    return state, story_beat
