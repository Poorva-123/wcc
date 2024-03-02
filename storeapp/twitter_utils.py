import tweepy
import os
from .models import TwitterAccount

def filter_tweets(tweets, keywords=None):
    if keywords is None:
        # Default banned words list
        banned_words = ['profanity', 'explicit', 'inappropriate']
    else:
        banned_words = keywords
    
    filtered_tweets = []
    for tweet in tweets:
        if any(word in tweet.text.lower() for word in banned_words):
            filtered_tweets.append(tweet)
    return filtered_tweets

def get_tweets(twitter_username):
    # Fetch Twitter API credentials from environment variables
    consumer_key = os.environ.get('8TEBrDnrnjMFpzaeW8U3LC1wl')
    consumer_secret = os.environ.get('Etyk6f8dA5RtwquPV90H4H0NgJQ7yWNty15otABjcaSsmD1Rgp')
    access_token = os.environ.get('1762905733601861632-fZwNDXiTUV9a6tzoofOSXXH8SWU8b6')
    access_token_secret = os.environ.get('hPoF4TO3z556RzmGpyLvsda4dixLM8d9KvaqFo4W2mSL6')

    # Authenticate with Twitter API
    auth = tweepy.OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch tweets from user's timeline
    tweets = api.user_timeline(screen_name=twitter_username, count=10)
    return tweets

def get_twitter_auth():
    # Implement your Twitter authentication logic here
    pass

def get_access_tokens(verifier_token):
    # Implement your logic to get access tokens here
    pass
