import datetime
import pickle
import pandas
import snscrape.modules.twitter as twitter

data_path = r".\data"


users = ["realDonaldTrump"]

for user in users:
    with open(data_path + "\\users\\" + user + ".pkl", "rb") as file:
        user_tweets = pickle.load(file)

    row_data = []

    for tweet in user_tweets:

        if (tweet.mentionedUsers is None):
            mentions = []
        else:
            mentions = [ mentioned_user.username for mentioned_user in tweet.mentionedUsers ]
        
        row_data.append([tweet.date, tweet.content, " ".join(mentions), tweet.likeCount, tweet.replyCount, tweet.retweetCount])

    tweet_df = pandas.DataFrame(row_data, columns = [ 'date', 'tweet_content', 'user_mentions', 'like_count', 'reply_count', 'retweet_count'])
    tweet_df.to_pickle( data_path + "/users/" + user + "_df.pkl")
        
        

"""

key_words = [
    "Trump", "Clinton"
]

for key_word in key_words:
    with open(data_path + "\\key_words\\" + key_word + ".pkl", "rb") as file:
        key_word_tweets = pickle.load(file)

"""
