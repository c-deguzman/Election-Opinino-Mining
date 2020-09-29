import datetime
import pickle
import snscrape.modules.twitter as twitter

data_path = r"C:\Users\cdegu\OneDrive\Documents\BMO 2020\Election-Opinion-Mining\twitter\data"
end_date = datetime.datetime(2016, 9, 1, 0, 0, tzinfo = datetime.timezone.utc)


# Scrape user list
users = [
    "realDonaldTrump",
    "hillaryclinton"
    ]

for user in users:

    user_tweets = []
    
    for i, tweet in enumerate(twitter.TwitterUserScraper(user).get_items()):
        
        user_tweets.append(tweet)

        if (tweet.date < end_date):
            break

        if (i % 250 == 0):
            print(tweet.content)
            print(tweet.date)
            print("From: " + tweet.username)
            print("Count: " + str(i))
            print("-" * 15)


    with open(data_path + "\\users\\" + user + ".pkl", "wb") as file:
        pickle.dump(user_tweets, file)
    
"""


KEY_WORDS = [
    "Trump", "Clinton",
    "Republicans", "Democrats",
    #"Biden", "Obama"
]

TWEET_LIMIT = 100

for key_word in KEY_WORDS:

    key_word_tweets = []
    
    for i, tweet in enumerate(twitter.TwitterSearchScraper(key_word +
                                                           ' lang:en').get_items()):
            print(tweet.content)
            print(tweet.date)
            print(tweet.likeCount)
            print("For: " + key_word)

            key_word_tweets.append(tweet)
            
            if (i >= TWEET_LIMIT - 1):
                    break

    with open(data_path + "\\key_words\\" + key_word + ".pkl", "wb") as file:
        pickle.dump(key_word_tweets, file)
    

"""
