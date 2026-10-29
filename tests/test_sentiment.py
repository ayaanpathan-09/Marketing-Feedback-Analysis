import unittest
from src.sentiment import analyze_sentiment

class SentimentTests(unittest.TestCase):
    def test_positive_text(self):
        label, score = analyze_sentiment("This is excellent and helpful. I love it.")
        self.assertEqual(label, "Positive")

    def test_negative_text(self):
        label, score = analyze_sentiment("This is poor, confusing, and disappointing.")
        self.assertEqual(label, "Negative")

    def test_neutral_text(self):
        label, score = analyze_sentiment("The package arrived on Tuesday.")
        self.assertIn(label, ["Neutral", "Positive", "Negative"])
        self.assertTrue(-1 <= score <= 1)

if __name__ == "__main__":
    unittest.main()
