from nltk.sentiment import SentimentIntensityAnalyzer
sentiment_analyzer=SentimentIntensityAnalyzer()
sentence="NLTK is a powerful library for natural language processing."
sentiment_score=sentiment_analyzer.polarity_scores(sentence)
print("Sentiment Score:",sentiment_score)
