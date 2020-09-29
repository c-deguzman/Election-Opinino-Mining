import praw

import settings
from enums import RedditAPI


reddit = praw.Reddit(
	client_id = settings.solve_env_field(RedditAPI.CLIENT_ID),
	client_secret = settings.solve_env_field(RedditAPI.CLIENT_SECRET),
	user_agent = settings.solve_env_field(RedditAPI.USER_AGENT),
	username = settings.solve_env_field(RedditAPI.USERNAME),
	password = settings.solve_env_field(RedditAPI.PASSWORD))


reddit.read_only = True

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)


subreddit = reddit.subreddit("redditdev")

