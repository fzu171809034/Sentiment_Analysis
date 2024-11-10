import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_csv('Black Myth.csv')

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores

#Delete URL,Mentions(@...)...
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+|www\.\S+', '',text)
    text = re.sub('@\\S+', '', text)

    return text


data['text'] = data['text'].apply(clean_text)
data[['negative', 'neutral', 'positive', 'compound']] = data['text'].apply(lambda text: pd.Series(analyze_sentiment(text)))


data.to_excel('Analysis.xlsx', index=False)


