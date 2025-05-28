import os
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Suppress symlink warning on Windows
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Load Transformer sentiment analysis model explicitly
transformer_sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    print(f"(TextBlob polarity score: {sentiment:.2f})")
    if sentiment < 0:
        return "Negative 😡"
    elif sentiment > 0:
        return "Positive 😊"
    else:
        return "Neutral 😐"

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)['compound']
    print(f"(VADER compound score: {sentiment:.2f})")
    if sentiment <= -0.05:
        return "Negative 😡"
    elif sentiment >= 0.05:
        return "Positive 😊"
    else:
        return "Neutral 😐"

def analyze_sentiment_transformers(text):
    result = transformer_sentiment(text)[0]
    label = result['label']
    score = result['score']
    print(f"(Transformers label: {label}, score: {score:.2f})")
    if label == "POSITIVE":
        return "Positive 😊"
    elif label == "NEGATIVE":
        return "Negative 😡"
    else:
        return "Neutral 😐"

def analyze_input():
    text = input("Enter sentence for analysis: ")
    print("Choose sentiment analysis method:")
    print("1. TextBlob")
    print("2. VADER")
    print("3. Transformers")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        print(f"TextBlob sentiment     : {analyze_sentiment_textblob(text)}")
    elif choice == "2":
        print(f"VADER sentiment        : {analyze_sentiment_vader(text)}")
    elif choice == "3":
        print(f"Transformers sentiment : {analyze_sentiment_transformers(text)}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    analyze_input()
