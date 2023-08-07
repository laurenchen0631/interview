import pandas as pd

# SELECT tweet_id
# FROM Tweets
# WHERE LENGTH(content) > 15

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    return df[['tweet_id']]