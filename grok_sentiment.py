# grok_sentiment.py - Simple Grok-style sentiment analyzer for text (e.g., news/tweets)
# Built by Grok for @RMJr92 - Free OSS tool, MIT license


import sys
import torch
from transformers import pipeline, BertTokenizer, BertForSequenceClassification

# Load FinBERT model (financial sentiment tuned)
model_name = 'yiyanghkust/finbert-tone'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

def get_sentiment_score(text):
    """
    Analyze text sentiment: Returns float score (-1.0 negative, 0 neutral, +1.0 positive)
    """
    if not text:
        return 0.0
    result = sentiment_analyzer(text)
    label = result[0]['label'].lower()
    score = result[0]['score']
    if 'positive' in label:
        return score
    elif 'negative' in label:
        return -score
    else:
        return 0.0  # Neutral

# Command-line runner (e.g., for quick tests)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python grok_sentiment.py 'Your text here'")
        sys.exit(1)
    text = ' '.join(sys.argv[1:])
    score = get_sentiment_score(text)
    print(f"Sentiment score: {score:.2f}")