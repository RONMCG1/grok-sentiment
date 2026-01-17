import unittest
from grok_sentiment import get_sentiment_score

class TestSentimentScore(unittest.TestCase):
    def test_positive(self):
        score = get_sentiment_score("Stocks are booming!")
        self.assertGreater(score, 0.5)

    def test_negative(self):
        score = get_sentiment_score("Market crashes hard.")
        self.assertLess(score, -0.5)

    def test_neutral(self):
        score = get_sentiment_score("The sky is blue.")
        self.assertAlmostEqual(score, 0.0, places=1)

if __name__ == '__main__':
    unittest.main()
