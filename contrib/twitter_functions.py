from tweepy import OAuthHandler
from tweepy import API
from django.conf import settings
from tweepy import Cursor


# Create Authentication object
def get_twitter_auth():
    print('Getting twitter Auth')
    authenticate = OAuthHandler(consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECRET)
    authenticate.set_access_token(key=settings.ACCESS_KEY, secret=settings.ACCESS_SECRET)
    api = API(authenticate, wait_on_rate_limit=True)
    print('Received Twitter auth')
    return api


def get_tweets_data(search_query):
    hashtag_list = search_query['hashtag_list']
    num_tweets = search_query['num_tweets']
    from_date = search_query['from_date']
    language = search_query['language']
    print('Scraping Tweets')
    if hashtag_list is None:
        hashtag_list = ['#Stadia', '@Stadia_r']
    api = get_twitter_auth()
    tweet_json_all = []
    print(f'from date --> {from_date}')
    for hashtag in hashtag_list:
        tweets = Cursor(api.search, hashtag, since=from_date, lang=language).items(num_tweets)
        json_data = [data._json for data in tweets]
        tweet_json_all = tweet_json_all + json_data
    print('Received Tweets JSON')
    return tweet_json_all


