#https://www.pluralsight.com/guides/building-a-twitter-sentiment-analysis-in-python
#https://towardsdatascience.com/text-classification-with-nlp-tf-idf-vs-word2vec-vs-bert-41ff868d1794

# for data
import json
import pandas as pd
import numpy as np

# for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# for processing
import re
import nltk

# for bag-of-words
from sklearn import feature_extraction, feature_selection, model_selection, naive_bayes, pipeline, manifold, preprocessing## for explainer
from lime import lime_text

# for word embedding
import gensim
import gensim.downloader as gensim_api

# for deep learning
from tensorflow.keras import models, layers, preprocessing as kprocessing
from tensorflow.keras import backend as K

# for bert language model
import transformers

import datetime
import pickle
import random
import snscrape.modules.twitter as twitter

HASH_TAG = "#"
MENTION = "@"

LST_STOPWORDS = nltk.corpus.stopwords.words("english")

def extract_tags(tweet_content: str) -> list:
    tweet_tokens = tweet_content.split(" ")
    tags = []

    if (HASH_TAG in tweet_content):
        # Pick out tags from tweets
        for tweet_token in tweet_tokens:

            if (HASH_TAG not in tweet_token):
                continue
            
            for idx, hash_start in enumerate(tweet_token.split(HASH_TAG)):
                if (idx == 0):
                    continue
                
                if (len(hash_start) > 1):
                    tags.append(hash_start)

    return tags


def extract_mentions(tweet_mentions: str) -> list:
    mentions = []

    if (tweet_mentions is not None):
        # Lowercase list of usernames
        for user in tweet_mentions:
            mentions.append(user.username.lower())

    return mentions


def utils_preprocess_text(text, flg_stemm=False, flg_lemm=True, lst_stopwords=None, tags=None, mentions=None, tcooutlinks=None):

    #Remove links
    if (tcooutlinks is not None):
        for outlink in tcooutlinks:
            text = text.replace(outlink, "")

    #Remove special characters
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
            
    lst_text = text.split()

    # remove Stopwords
    if (lst_stopwords is not None):
        lst_text = [word for word in lst_text if word not in 
                    lst_stopwords]

    # Remove twitter tags
    if (tags is not None):
        lst_text = [word for word in lst_text if word not in tags]

    # Remove mentions
    if (mentions is not None):
        lst_text = [word for word in lst_text if word not in mentions]

    # Stemming (remove -ing, -ly, ...)
    if (flg_stemm == True):
        ps = nltk.stem.porter.PorterStemmer()
        lst_text = [ps.stem(word) for word in lst_text]
                
    # Lemmatisation (convert the word into root word)
    if (flg_lemm == True):
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        lst_text = [lem.lemmatize(word) for word in lst_text]
            
    text = " ".join(lst_text)
    return text
    

data_path = r"C:\Users\cdegu\OneDrive\Documents\BMO 2020\Election-Opinion-Mining\twitter\data"

key_words = ["Trump", "Republicans", "Democrats"]


full_text_list = []
tweet_ids = set()


for key_word in key_words:
    # Get raw data
    with open(data_path + "\\key_words\\" + key_word + ".pkl", "rb") as file:
            key_word_tweets = pickle.load(file)

    print("Starting: " + key_word)

    for tweet in key_word_tweets:
        tags = extract_tags(tweet.content.lower())
        mentions = extract_mentions(tweet.mentionedUsers)
        tcooutlinks = tweet.tcooutlinks

        clean_text = utils_preprocess_text(tweet.content, False, True, LST_STOPWORDS, tags, mentions, tcooutlinks)
        
        full_text = clean_text + " | " + " ".join(tags) + " | " + " ".join(mentions)

        if ( tweet.id not in tweet_ids ):
            tweet_ids.add(tweet.id)
            full_text_list.append((full_text, tweet.content))

"""
# Manual Training
random.shuffle(full_text_list)

classified = []

for idx, pair in enumerate(full_text_list):
    if ( idx > 100 ):
        break

    print("-" * 10)
    print(pair[1])

    # 5 = trump supporter
    # 4 = republican leaning
    # 3 = neutral
    # 2 = democrat leaning
    # 1 = trump hater
    score = int(input())

    classified.append([score, pair[0], pair[1]])

# Store training data
with open(data_path + "\\key_words\\classified data\\Democrat_Trump_Republican.pkl", "wb") as file:
	pickle.dump(classified, file)

"""

# Open training data
with open(data_path + "\\key_words\\classified data\\Democrat_Trump_Republican-training_df.pkl", "rb") as file:
	training_df = pickle.load(file)



# Create the testing_df
training_entries = set()
training_df['full_text'].apply(lambda val: training_entries.add(val))

testing_list = []

for item in full_text_list:
    if (item[1] not in training_entries):
        testing_list.append([item[0], item[1]])

testing_df = pd.DataFrame(testing_list, columns = ['clean_text', 'full_text'])



"""
for key_word in key_words:
    # Get raw data
    with open(data_path + "\\key_words\\" + key_word + ".pkl", "rb") as file:
        key_word_tweets = pickle.load(file)
        for tweet in key_word_tweets:
            if (tweet.content == testing_df.iloc[0]['full_text']):
                tweet_target = tweet
                break
"""
