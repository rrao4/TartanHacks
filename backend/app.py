from flask import Flask, request, jsonify
from game_logic import start_game, process_turn
from perplexity_api import query_perplexity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access the backend

@app.route('/')
def index():
    return "Welcome to the AI Story API. Use /nextBeat to continue the story."

@app.route('/start', methods=['POST'])
def start():
    # Initialize game state
    game_state = start_game()
    return jsonify(game_state)

@app.route('/nextBeat', methods=['POST'])
def next_beat():
    data = request.get_json()
    user_input = data.get('user_input', '').strip()  # Ensure we get a valid string
    current_state = data.get('state', {})  # Game state (optional)

    if not user_input:
        return jsonify({'error': 'User input is required'}), 400

    # Generate new story continuation using Perplexity
    prompt = f"Game state: {current_state}\nUser input: {user_input}\nContinue the story in one short paragraph:"
    story_beat = query_perplexity(prompt)  # Call Perplexity API

    return jsonify({'state': current_state, 'story_beat': story_beat})

if __name__ == '__main__':
    app.run(debug=True)