import unittest
from game_logic import start_game, process_turn

class TestGameLogic(unittest.TestCase):
    def test_start_game(self):
        state = start_game()
        self.assertEqual(state['beat_count'], 0)
        self.assertEqual(state['history'], [])
    
    def test_process_turn(self):
        state = start_game()
        state, beat = process_turn(state, "Test input")
        self.assertEqual(state['beat_count'], 1)
        self.assertIn("Placeholder narrative", beat)

if __name__ == '__main__':
    unittest.main()
