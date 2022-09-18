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

# client = tweepy.Client(consumer_key=api_key,
#                        consumer_secret=api_key_secret,
#                        access_token=access_token,
#                        access_token_secret=access_token_secret)

# public_tweets = client.get_users_tweets(id=802064401, 
#                                         user_auth=True,tweet_fields = ["created_at", "text", "source"],
#                                         user_fields = ["name", "username", "location", "verified", "description"],
#                                         max_results = 10,
#                                         expansions='author_id')

# print(public_tweets.data[0])