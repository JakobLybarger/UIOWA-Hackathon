import praw
from textblob import TextBlob
import nltk
import credentials # import the credential 
import re
import pickle

# # Download the VADAR tool and access it through the NLTK library.
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer 


reddit = praw.Reddit(client_id=credentials.client_id,
                         client_secret=credentials.client_secret,
                         user_agent=credentials.user_agent)




class Ticker(): ## ticker class, the dict is such that the key is a ticker and the value is a dict
    def __init__(self,ticker,full_name,sector):
        self.ticker = ticker # ticker ex: TSLA
        self.full_name = full_name # full name of the company
        self.sector = sector # sector of the ticker
        self.comments = [] # list of comment objects provided by PRAW

# get tickers from the csv
def get_tickers(file_name) -> dict:
    tickers = {} # dict where the ticker is the key and the value is a tuple of (full)
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        split_line = line.split(",")
        ticker = split_line[0]
        company = split_line[1]
        sector = split_line[2]
        tickers[ticker] = Ticker(ticker, company, sector)
    return tickers

def get_posts(target_subreddit, post_limit) -> dict:
    tickers = get_tickers("tickers.txt") # get the ticker dict
    posts = reddit.subreddit(target_subreddit).new(limit=post_limit)
    count = 0
    for post in posts:   #iterate through posts
        if "GME" not in post.title:
            count += 1
            print(count)
            try:
                post.comments.replace_more(limit=None) # this generates a tree of comments that is iteratable
                for comment in post.comments.list():
                    for word in str(comment.body).split(" "): #iterate through each word in the comment, .split() creates an array of words instead of iterating through charecters
                        word = re.sub(r'\W+','', word) #remove charecters that we dont care about
                        if word in tickers.keys(): # see if the currrent word is a valid ticker
                            tickers[word].comments.append(comment) # if so, append the comment to the object stored at tickers[word]
                            
            except Exception as E: #ghetto error handling
                print(E)
                continue
    #save the dict locally for further processing
    pkl_file = open("tickers.pkl", "wb")
    pickle.dump(tickers, pkl_file)




if __name__ == "__main__":
    #tickers = get_tickers("tickers.txt")
    get_posts("investing", 1000)
    #get_tickers("tickers.txt")
