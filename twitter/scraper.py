import datetime
import pickle
import snscrape.modules.twitter as twitter

data_path = r"C:\Users\cdegu\OneDrive\Documents\BMO 2020\Election-Opinion-Mining\twitter\data"
end_date = datetime.datetime(2020, 9, 1, 0, 0, tzinfo = datetime.timezone.utc)


# Scrape user list

# Already did for "realDonaldTrump
users = ["realDonaldTrump"]

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
            print("-" * 15)


    with open(data_path + "\\" + user + ".pkl", "wb") as file:
        pickle.dump(user_tweets, file)
    


"""
for i, tweet in enumerate(twitter.TwitterSearchScraper('corona lang:en').get_items()):
	print(tweet)
	if (i >= 49):
		break

"""
