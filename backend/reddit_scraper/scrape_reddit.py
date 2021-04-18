import praw
import pickle
import pandas as pd
import sys
import os
import credentials

# open the instance of praw (reddit's api)
reddit = praw.Reddit(client_id=credentials.client_id,
                        client_secret=credentials.client_secret,
                        user_agent=credentials.user_agent)


def get_comments(target_subreddit, period) -> list: # returns a list of all comments on the target subreddit for posts in range post_limit
    comments = []
    

    posts = reddit.subreddit(target_subreddit).new(limit = None)
    count = 0
    for post in posts:  # iterate through posts
        print("Getting comments... currently on post " , count)
        count += 1
        try:
            post.comments.replace_more(limit=0) # this generates a tree of comments that is iteratable
            for comment in post.comments.list():
                comments.append(comment)
                

        except Exception as E:  # ghetto error handling
            print("error" + E)
            continue
    return comments



def write_pickle(posts, filename):
    outfile = open(filename, "wb")
    pickle.dump(posts, outfile)


def open_tickers(filename):
    return pd.read_pickle(filename)


def scrape(target_subreddit, period):
    period = "1Y"
    print("Scraping " + target_subreddit + " for the last " + period)
    outfile = target_subreddit + "_" + period + ".pkl"
    if not os.path.exists(outfile):
        comments = get_comments(target_subreddit, period)
        write_pickle(comments, outfile)
    else:
        print("Done scraping!")
    return outfile

if __name__ == "__main__":
    scrape(sys.argv[1], sys.argv[2])
