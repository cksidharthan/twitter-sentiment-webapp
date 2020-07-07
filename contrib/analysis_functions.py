

def get_sentiment(dataframe):
    print('Analysing sentiments')
    sentiment_dict = {
        'Neutral': len(dataframe[dataframe['sentiment'] == 0]),
        'Weakly_Positive': len(dataframe[(dataframe['sentiment'] > 0) & (dataframe['sentiment'] <= 0.3)]),
        'Positive': len(dataframe[(dataframe['sentiment'] > 0.3) & (dataframe['sentiment'] <= 0.6)]),
        'Strongly_Positive': len(dataframe[(dataframe['sentiment'] > 0.6) & (dataframe['sentiment'] <= 1)]),
        'Weakly_Negative': len(dataframe[(dataframe['sentiment'] > -0.3) & (dataframe['sentiment'] < 0)]),
        'Negative': len(dataframe[(dataframe['sentiment'] > -0.6) & (dataframe['sentiment'] <= -0.3)]),
        'Strongly_Negative': len(dataframe[(dataframe['sentiment'] >= -1) & (dataframe['sentiment'] <= -0.6)])
    }
    print('Sentiment analysis Done')
    return sentiment_dict


def get_tweet_source_dict(dataframe):
    source_dict = {}
    source = dict(dataframe['source'].value_counts())
    # Order source by descending order and return the top 6 sources
    sorted_dict = sorted(source.items(), key=lambda x: x[1], reverse=True)[0:6]
    for source, value in sorted_dict:
        source_dict[source] = value
    return source_dict
