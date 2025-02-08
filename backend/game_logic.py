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
    # print(f"before: {state['history']}")

    # Append user's message to history
    state['history'].append({"role": "user", "content": user_input})

    # Check if the story should restart
    if state['beat_count'] >= 10:
        return start_game(), "The story has reached its conclusion. Starting a new adventure..."

    # Construct a string from state["history"]
    s = "\n".join([f'{msg["role"].capitalize()}: {msg["content"]}' for msg in state["history"]])
    print(s)
    n = state["beat_count"]
    print(n)
    messages = [{
        "role": "system",
        "content": '''This game is a “choose your own adventure”.
        You are to engage with the player and create a story around their responses and a 
        central theme. This game is to be very eccentric and intriguing. Maintain a consistent, 
        narrative tone that changes with the seriousness of the player. You should subvert 
        the player’s actions only when absolutely neccessary.

        There are only 10 story ‘blocks’ allowed, or total computer responses. The story should include 
        a climax and naturally conclude with any ending that makes sense (or doesn't, if it comes to that). Responses should not include 
        interpretations or feelings about the environment or lead players to a decision, but rather leave open-ended opportunities.

        The total number of ‘blocks’ is 10. Do not exit the game. Even if subverting a 
        nonsensical input, try and incorporate elements of the player's response.

        The current ‘block’ is''' + str(n) + '''
        The current story so far:''' + s + '''If there is no current story, invent a new beginning that corresponds to the theme.
        You are to play this game with me. Only return the text that I can respond to as a player. Respond using a max of 5 sentences.

        The theme is: happiness
        ''' 
    }] + state["history"]

    #messages = [{"role": "system", "content": '''Be precise and concise.'''}] + state["history"]
    
    # Generate AI response
    ai_response = query_perplexity(messages)

    # Append AI response to history
    state['history'].append({"role": "assistant", "content": ai_response})

    # Increment beat count
    state['beat_count'] += 1
    # print(f"after: {state['history']}")
    # print("-----------")

    return state, ai_response
