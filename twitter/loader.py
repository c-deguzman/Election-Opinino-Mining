import datetime
import pickle
import snscrape.modules.twitter as twitter

data_path = r"C:\Users\cdegu\OneDrive\Documents\BMO 2020\Election-Opinion-Mining\twitter\data"

"""
users = ["realDonaldTrump"]

for user in users:
    with open(data_path + "\\users\\" + user + ".pkl", "rb") as file:
        user_tweets = pickle.load(file)

"""

key_words = [
    "Trump", "Clinton"
]

for key_word in key_words:
    with open(data_path + "\\key_words\\" + key_word + ".pkl", "rb") as file:
        key_word_tweets = pickle.load(file)

