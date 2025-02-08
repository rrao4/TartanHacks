from flask import Flask, request, jsonify
from config import Config
from game_logic import start_game, process_turn
from perplexity_api import query_perplexity

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return "Welcome to the Text-Based Game API. Use /start to begin a game."

@app.route('/start', methods=['POST'])
def start():
    # Initialize game state
    game_state = start_game()
    return jsonify(game_state)

@app.route('/nextBeat', methods=['POST'])
def next_beat():
    data = request.get_json()
    user_input = data.get('user_input', '')
    current_state = data.get('state', {})
    # Process game turn
    updated_state, story_beat = process_turn(current_state, user_input)
    return jsonify({'state': updated_state, 'story_beat': story_beat})

if __name__ == '__main__':
    app.run(debug=True)
