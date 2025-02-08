import unittest
from perplexity_api import query_perplexity

class TestPerplexityAPI(unittest.TestCase):
    def test_query_perplexity(self):
        # Note: In a real test, you would mock requests.post
        prompt = "Test prompt"
        response = query_perplexity(prompt)
        self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()
