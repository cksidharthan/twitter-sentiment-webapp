import pandas as pd
import plotly.express as px
from plotly.offline import plot
from wordcloud import WordCloud, STOPWORDS
from contrib import helper_functions

config = {
    'displaylogo': False,
    'modeBarButtonsToAdd': ['drawline', 'drawrect', 'eraseshape'],
}


def get_tweet_count_over_time_graph(dataframe):
    print('Creating Tweets over time graph')
    date_frame = pd.DataFrame(columns=['date_time', 'count'])
    date_time_data = dataframe['date_time'].value_counts()
    for key, value in date_time_data.items():
        new_dict = {'date_time': key, 'count': value}
        date_frame = date_frame.append(new_dict, ignore_index=True)
    date_frame = date_frame.sort_values(by=['date_time'], ascending=True)
    graph = px.line(date_frame, x='date_time', y='count')
    graph.update_layout(autosize=True, xaxis_title='Date & Time', yaxis_title='Tweet Count')
    graph.update_traces(mode="markers+lines")
    plot_div = plot(graph, output_type='div', config=config)
    print('Created Tweets Over time graph')
    return plot_div


def get_wordcloud(dataframe):
    print('Generating tweet Wordcloud')
    tweet_words = ' '.join([tweets for tweets in dataframe['tweet_text']])
    no_urls_no_tags = " ".join(
        [word for word in tweet_words.split() if 'http' not in word and not word.startswith('@') and word != 'RT'])
    tweet_wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=1800, height=1400,
                                max_words=50).generate(no_urls_no_tags)
    uri = helper_functions.convert_plot_to_uri(tweet_wordcloud)
    print('Generated Tweet Wordcloud')
    return uri


def get_weekly_breakdown(dataframe):
    print('Calculating Weekly breakdown')
    tweet_by_day_data = dataframe['day'].value_counts()
    days = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    for key, value in tweet_by_day_data.items():
        for day, count in days.items():
            if day[0:3] == key:
                days[day] = value
    print('Weekly breakdown calculation completed')
    return days


def get_hashtag_cloud(dataframe):
    hashtag_dict = {}
    tweet_hashtag_list = []
    for hashtag_list in dataframe['hashtags']:
        if len(hashtag_list) > 0:
            for hashtag in hashtag_list:
                tweet_hashtag_list.append(hashtag)
    hashtag_df = pd.DataFrame({'hashtag': tweet_hashtag_list})
    hashtags = dict(hashtag_df['hashtag'].value_counts())
    hashtag_sorted_dict = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    for hashtag, value in hashtag_sorted_dict:
        hashtag_dict[hashtag] = value
    wordcloud = WordCloud(width=1800, height=1400, background_color='white', max_words=500,
                          collocations=False).generate_from_frequencies(hashtag_dict)
    uri = helper_functions.convert_plot_to_uri(wordcloud)
    return uri


def get_top_tweeters(dataframe):
    tweeter_dict = {}
    tweeter = dict(dataframe['screenname'].value_counts())
    tweeter_sorted_dict = sorted(tweeter.items(), key=lambda x: x[1], reverse=True)
    for tweeter, value in tweeter_sorted_dict:
        tweeter_dict[tweeter] = value
    top_tweeter_wordcloud = WordCloud(width=1800, height=1400, background_color="white", max_words=50,
                                      collocations=False).generate_from_frequencies(tweeter_dict)
    uri = helper_functions.convert_plot_to_uri(top_tweeter_wordcloud)
    return uri


# need to refactor
def get_geomap(dataframe):
    locs = dataframe['location'].value_counts()
    locs = list(locs.index)
    if "" in locs:
        locs.remove('')
    geolocated = helper_functions.get_geocode_city(locs[0:10])
    geolocated = pd.DataFrame(geolocated)
    geolocated.columns = ['location', 'latlong']
    geolocated = geolocated.dropna()
    geolocated['lat'] = geolocated.latlong.apply(lambda x: x[0])
    geolocated['lon'] = geolocated.latlong.apply(lambda x: x[1])
    geolocated.drop('latlong', axis=1, inplace=True)
    mapdata = pd.merge(dataframe, geolocated, how='inner', left_on='location', right_on='location')
    fig = px.scatter_mapbox(mapdata, lat="lat", lon="lon", hover_name="location",
                                hover_data=["location", "sentiment"],
                                color_discrete_sequence=["fuchsia"], zoom=0, height=500, color="sentiment",
                                size="map_marker_size")
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    plot_div = plot(fig, output_type='div', config=config)
    return plot_div


def get_sentiment_timeline(dataframe):
    new_dataframe = dataframe[['tweet_text', 'screenname', 'sentiment', 'date_time']]
    date_frame = new_dataframe.sort_values(by=['date_time'], ascending=True)
    graph = px.line(date_frame, x='date_time', y='sentiment', hover_name="screenname",
                    hover_data=['tweet_text', 'date_time', 'sentiment'])
    graph.update_layout(autosize=True, xaxis_title='Date & Time', yaxis_title='Sentiment')
    graph.update_traces(mode="markers+lines")
    graph.update_layout(hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"))
    plot_div = plot(graph, output_type='div', config=config)
    return plot_div
