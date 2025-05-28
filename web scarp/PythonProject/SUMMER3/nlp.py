from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < 0:
        return "Negative 😡"
    elif sentiment > 0:
        return "Positive 😊"
    else:
        return "Neutral 😐"

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)['compound']
    if sentiment <= -0.05:
        return "Negative 😡"
    elif sentiment >= 0.05:
        return "Positive 😊"
    else:
        return "Neutral 😐"

def analyze_input():
    text = input("Enter sentence for analysis: ")
    print(f"TextBlob sentiment : {analyze_sentiment_textblob(text)}")
    print(f"VADER sentiment    : {analyze_sentiment_vader(text)}")


analyze_input()
