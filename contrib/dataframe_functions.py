import pandas as pd
import time
import re
from textblob import TextBlob


def create_new_dataframe():
    columns = ['created_at', 'date_time', 'day', 'date', 'time', 'user_id', 'screenname', 'user_full_name',
               'tweet_text', 'hashtags', 'location',
               'followers_count', 'retweet_count', 'favourites_count', 'source', 'map_marker_size']
    tweet_dataframe = pd.DataFrame(columns=columns)
    return tweet_dataframe


def get_dataframe_row_values(tweet_json_data):
    tweet_dict = {}
    try:
        tweet_dict['created_at'] = tweet_json_data['created_at']
        tweet_dict['date_time'] = time.strftime('%Y-%m-%d %H:%M', time.strptime(tweet_json_data['created_at'],
                                                                                '%a %b %d %H:%M:%S +0000 %Y'))
        tweet_dict['day'] = tweet_json_data['created_at'][:3]
        tweet_dict['date'] = time.strftime('%Y-%m-%d',
                                           time.strptime(tweet_json_data['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        tweet_dict['time'] = time.strftime('%H:%M:%S',
                                           time.strptime(tweet_json_data['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        tweet_dict['user_id'] = tweet_json_data['id']
        tweet_dict['screenname'] = '@' + tweet_json_data['user']['screen_name']
        tweet_dict['user_full_name'] = tweet_json_data['user']['name']
        tweet_dict['tweet_text'] = tweet_json_data['text']
        tweet_dict['hashtags'] = list(['#' + hashtag['text'] for hashtag in tweet_json_data['entities']['hashtags']])
        tweet_dict['location'] = tweet_json_data['user']['location']
        tweet_dict['followers_count'] = tweet_json_data['user']['followers_count']
        tweet_dict['retweet_count'] = tweet_json_data['retweet_count']
        tweet_dict['favourites_count'] = tweet_json_data['favorite_count']
        tweet_dict['source'] = re.findall(r'<a[^>]*>(.*?)</a>', tweet_json_data['source'])[0]
        tweet_dict['map_marker_size'] = 0.1
    except:
        print('Invalid entry')
    return tweet_dict


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analyze_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    return analysis.sentiment.polarity


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


def get_polarity(text):
    return TextBlob(text).sentiment.polarity
