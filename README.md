# Grok-Sentiment: Simple AI Sentiment Analyzer

Grok-style tool for analyzing text sentiment (positive, negative, or neutral scores). Tuned with FinBERT for finance/trading vibes, but works on any text like news or tweets.
[![Stars](https://img.shields.io/github/stars/RONMCG1/grok-sentiment?style=social)](https://github.com/RONMCG1/grok-sentiment/stargazers)
## Why This Tool?
- Quick sentiment scores: -1.0 (very negative) to +1.0 (very positive), 0 for neutral.
- Easy for devs/traders: Plug into bots, scripts, or command line.
- Open-source (MIT license) – fork it, use it, no strings.

Built as a nod to Grok/xAI – if you're in Bastrop or AI scene, hit me up.

## Installation
1. Install dependencies:
2. pip install transformers torch
3. 2. Download `grok_sentiment.py` from this repo.

## Usage
### As a Library
```python
from grok_sentiment import get_sentiment_score

text = "Stocks are booming today!"
score = get_sentiment_score(text)
print(f"Sentiment: {score:.2f}")  # e.g., 0.95
python grok_sentiment.py "Market crashes hard"
# Output: Sentiment score: -0.98
