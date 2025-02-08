from perplexity_api import query_perplexity

def start_game():
    """Initialize a new game session with an empty history."""
    return {
        'beat_count': 0,  # number of turns
        'history': [],  # current story history for context
    }

def process_turn(state, user_input):
    """Process the user's input and generate the next story beat."""

    # Append user's message to history
    state['history'].append({"role": "user", "content": user_input})

    # Check if the story should restart
    if state['beat_count'] >= 8:
        return start_game(), "The story has reached its conclusion. Starting a new adventure..."

    # Construct a string from state["history"]
    s = "\n".join([f'{msg["role"].capitalize()}: {msg["content"]}' for msg in state["history"]])
    n = state["beat_count"]
    messages = [{
        "role": "system",
        "content": '''This game is a “choose your own adventure” style game, but the twist is that the player can do whatever
        they like, and do not need to choose from predetermined options.
        You are to engage with the player and create a story around their responses and a 
        central theme. This game is to be very eccentric and intriguing. Maintain a consistent, 
        narrative tone that changes with the seriousness of the player. You should subvert 
        the player’s actions only when absolutely neccessary. Even if subverting a nonsensical input, try and incorporate elements of the player's response. The player is to be engaged, and their
        actions should have consequences. For example, if the player gets into fatal danger, they must be careful 
        or they may be injured or die. If the player is in a safe environment, they can be more relaxed. If the player
        has made a romantic blunder or choice, they should be teased or congratulated. Etc.

        There are only 8 story ‘blocks’ allowed, or total computer responses. Based on the current story beat, 
        the next event should be in the beginning, climax, or ending as appropriate. For example, the beginning 2 or 3
        story beats should be setup/beginning, the next 2 to 3 should be rising action ending with climax, and the final 1 to 2
        should be wrap-up for the story.

        The total number of ‘blocks’ is 8. 

        The current ‘block’ is''' + str(n) + '''! (Again, ''' + str(n) + ''' is the current block number!!!!!).

        If current block is equal to 7, your next response will be the ending. It should end with "The end."

        The current story so far is:''' + s + ''' 
        If there is no current story, invent a new beginning that corresponds to the theme. However, immerse the user.
        Don't say anything like "You typed...", and do not make reference to the fact you are an AI taking in input.
        You are to play this game with me. Only return the text that I can respond to as a player. Respond using a max of 7 sentences (this is very important).

        NEVER exit the game ever and respond as a normal chatbot. You must always be in character.

        The theme will be whatever the player types in initially.
        ''' 
    }] + state["history"]
    
    ai_response = query_perplexity(messages)

    # Append AI response to history
    state['history'].append({"role": "assistant", "content": ai_response})

    state['beat_count'] += 1
    return state, ai_response
