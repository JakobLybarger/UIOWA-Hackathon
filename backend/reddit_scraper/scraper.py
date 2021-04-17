import praw
from textblob import TextBlob
import nltk
import credentials # import the credential 

# Download the VADAR tool and access it through the NLTK library.
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer 


reddit = praw.Reddit(client_id=credentials.client_id,
                         client_secret=credentials.client_secret,
                         user_agent=credentials.user_agent)




# class ticker():
#     def __init__(self,ticker)

# get tickers from the csv
def get_tickers(file_name):
    tickers = {} # dict where the ticker is the key and the value is a tuple of (full)
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        split_line = line.split(",")
        ticker = split_line[0]
        company = split_line[1]
        sector = split_line[2]
        tickers[split_line[0]] = 0
        print("Ticker: " + ticker + " Full name: " + company + "sector: " + sector)

def get_posts(target_subreddit, post_limit, time_frame) -> dict:
    tickers = {} #dict where the ticker is the key and the comments are the values
    posts = reddit.subreddit(target_subreddit).new(limit=post_limit)
    for post in posts:   #iterate through posts
        try:
            post.comments.replace_more(limit=None)
            for comment in post.comments.list():
                print(comment.body)
            continue

def evaulate_comment(comment) -> int: #evaluates the comment, returns an integer from -1 to +1 indicating it's signifigance



if __name__ == "__main__":
    get_posts("wallstreetbets", 100, "week")
    #get_tickers("tickers.txt")
