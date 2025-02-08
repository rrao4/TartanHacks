from flask import Flask, request, jsonify
from game_logic import start_game, process_turn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# global game state
game_state = start_game()

@app.route('/')
def index():
    return "Welcome to the AI Story API. Use /nextBeat to continue the story."

@app.route('/start', methods=['POST'])
def start():
    """Manually reset the game state if needed."""
    global game_state
    game_state = start_game()  # Reset state
    return jsonify(game_state)

@app.route('/nextBeat', methods=['POST'])
def next_beat():
    """Continue the story and restart after 10 turns."""
    global game_state

    data = request.get_json()
    user_input = data.get('user_input', '').strip()

    if not user_input:
        return jsonify({'error': 'User input is required'}), 400

    # Generate response and update game state
    game_state, story_beat = process_turn(game_state, user_input)

    return jsonify({'state': game_state, 'story_beat': story_beat})

if __name__ == '__main__':
    app.run(debug=True)
