from config import *
import tweepy
import datetime

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=1)
tweets_list = tweepy.Cursor(api.search, q="#WeLoveGoats",tweet_mode='extended', lang='es').items(5)
output = []
for tweet in tweets_list:
    text = tweet._json["full_text"]
    # print(text)
    # favourite_count = tweet.favorite_count
    # retweet_count = tweet.retweet_count
    # created_at = tweet.created_at
    coordinates = tweet.place.bounding_box.coordinates
    # 'text' : text,

    line = {'coordinates' : coordinates[0][0]}
    print(line)
    output.append(line)
