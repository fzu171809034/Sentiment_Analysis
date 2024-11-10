import pandas as pd
import tweepy
from win32comext.adsi.demos.search import search

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAO9pwwEAAAAAG3jb7jzeh4ad%2BRVBd26je7BVUOA%3Dz4ALpPfZ6quvpZAoXWEuZirO7bHira7RCbTbDbJZXgAccXniIc'

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(keyword, count = 10):
    tweets = client.search_recent_tweets(query=keyword, max_results=count,
                                         tweet_fields=['created_at', 'public_metrics'])
    if tweets.data:
        tweet_data = [
            {
                'created_at': tweet.created_at,
                'text': tweet.text if hasattr(tweet, 'text') else None,
                'public_metrics': tweet.public_metrics,
            }
            for tweet in tweets.data
        ]
        DATA_1 = pd.DataFrame(tweet_data)
        return DATA_1
    else:
        print('No tweets found.')
        return pd.DataFrame()

tweets = fetch_tweets('Black Myth', 80)
if not tweets.empty:
    tweets.to_excel('Black Myth.xlsx', index=False)
    print(tweets.head())
else:
    print('no data to save.')




