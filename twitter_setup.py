import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
# bearer_token = config['twitter']['bearer_token']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# print(api_key)

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets[0])


# print(public_tweets.data[0])