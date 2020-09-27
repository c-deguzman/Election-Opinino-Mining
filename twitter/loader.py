import datetime
import pickle
import snscrape.modules.twitter as twitter

data_path = r"C:\Users\cdegu\OneDrive\Documents\BMO 2020\Election-Opinion-Mining\twitter\data"

users = ["realDonaldTrump"]

for user in users:
    with open(data_path + "\\" + user + ".pkl", "rb") as file:
        user_tweets = pickle.load(file)
