from contrib import helper_functions


def call_sentiment_function(search_query):
    twitter_dataframe = helper_functions.prepare_tweet_dataframe(search_query)
    analysis_results = helper_functions.sentiment_analysis(twitter_dataframe)
    return analysis_results


def create_context(analysis_results):
    search_text_list = []
    context = {
        'positive_tweets': analysis_results['sentiment']['Positive'] +
                           analysis_results['sentiment']['Strongly_Positive'] +
                           analysis_results['sentiment']['Weakly_Positive'],
        'negative_tweets': analysis_results['sentiment']['Negative'] +
                           analysis_results['sentiment']['Strongly_Negative'] +
                           analysis_results['sentiment']['Weakly_Negative'],
        'neutral_tweets': analysis_results['sentiment']['Neutral'],
        'sentiment_keys': list(analysis_results['sentiment'].keys()),
        'sentiment_values': list(analysis_results['sentiment'].values()),
        'search_text_list': search_text_list,
        'tweet_timeline_graph': analysis_results['tweet_timeline_graph'],
        'weekly_breakdown_keys': list(analysis_results['weekly_breakdown'].keys()),
        'weekly_breakdown_values': list(analysis_results['weekly_breakdown'].values()),
        'total_tweets': analysis_results['total_tweets'],
        'tweet_text_cloud': analysis_results['tweet_text_cloud'],
        'tweet_screenname_cloud': analysis_results['tweet_screenname_cloud'],
        'tweet_location_map': analysis_results['tweet_location_map'],
        'hashtag_cloud': analysis_results['hashtag_cloud'],
        'tweet_source_keys': list(analysis_results['tweet_source'].keys()),
        'tweet_source_values': list(analysis_results['tweet_source'].values()),
        'total_favourites': analysis_results['total_favourites'],
        'total_retweets': analysis_results['total_retweets'],
        'total_reach': analysis_results['total_reach'],
        'unique_users': analysis_results['unique_users'],
        'sentiment_timeline': analysis_results['sentiment_timeline'],
    }
    return context
