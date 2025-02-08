from perplexity_api import query_perplexity

def start_game():
    """Initialize a new game session with an empty history."""
    return {
        'beat_count': 0,  # Counts turns
        'history': [],  # Stores user and AI messages
        'theme': None  # Can be set dynamically later
    }

def process_turn(state, user_input):
    """Process the user's input and generate the next story beat."""
    print(f"before: {state['history']}")

    # Append user's message to history
    state['history'].append({"role": "user", "content": user_input})

    # Check if the story should restart
    if state['beat_count'] >= 10:
        return start_game(), "The story has reached its conclusion. Starting a new adventure..."

    # Create the conversation context
    messages = [{"role": "system", "content": "Be precise and concise."}] + state["history"]
    
    # Generate AI response
    ai_response = query_perplexity(messages)

    # Append AI response to history
    state['history'].append({"role": "assistant", "content": ai_response})

    # Increment beat count
    state['beat_count'] += 1
    print(f"after: {state['history']}")
    print("-----------")

    return state, ai_response
