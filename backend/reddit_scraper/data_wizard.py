from ast import parse
from typing import Text
import pandas as pd
import re
import pickle
import pandas as pd
import sys
from textblob import TextBlob, sentiments
from datetime import datetime
import time
import yfinance as yf
from pandas_datareader import data
import scrape_reddit

class Stock():  # ticker class, the dict is such that the key is a ticker and the value is a dict
    def __init__(self, ticker, name, sector, time_frame):
        self.name = name # full name of the stock ex: TSLA
        self.ticker = ticker  # ticker ex: TSLA
        self.sector = sector # sector of the stock EX: Automotive
        self.time_frame = time_frame # tuple where the first element is the start UNIX time stamp, last index is the end UNIX time stamp ex: (1609480800,1618754011)
        self.sentiment = None # average sentiment from the comments as determined by
        self.mentions = 0
        self.date_data = None # dict where the key is the date, value = (price, num_mentions)

class Comment():
    def __init__(self, date_posted, num_upvotes, sentiment):
        self.date_posted = date_posted # in the same format as yahoo finance ex: 2021-01-04
        self.num_upvotes = num_upvotes
        self.sentiment = sentiment

class Comments():
    def __init__(self,unix_time_range):
        self.unix_time_range = unix_time_range
        self.comments = []


#this builds the empty ticker dict
def build_ticker_dict(file_name, time_frame) -> dict: # generate our empty dict where the key is the ticker and the value is an instance of our class
    # dict where the ticker is the key and the value is a tuple of (full)
    tickers = {}
    file = open(file_name)
    lines = file.readlines()
    for line in lines:
        split_line = line.split(",")
        ticker = split_line[0]
        company_name = split_line[1]
        sector = split_line[2]
        tickers[ticker] = Stock(ticker, company_name, sector, time_frame)
    return tickers


# this function iterates through the tickers and creates the data data for each ticker at every day in period.  Period may be "1Y".
# data data is a list of tuples in form (date, price_on_that_day, num_mentions_on_that_day)
def get_date_data(tickers, plain_text_date, parsed_comments) -> dict:
    
    count = 0
    for ticker in tickers.keys(): #iterate through the keys
        print("Getting date data for " + ticker + ", " , (count / len(tickers.keys()) * 100), " percent complete")
        date_data = []
        count += 1
        sentiment = 0
        total_mentions = 0

        stock = yf.Ticker(ticker) # yahoo finance module, get ticker instance
        stock_history =  (stock.history(start=plain_text_date[0], end= plain_text_date[1]))

        for index, row in stock_history.iterrows():
            current_day = str(index.date())
            day_sentiment, num_mentions = get_comment_data(parsed_comments, ticker,current_day) # get comment data for that day
            total_mentions += num_mentions
            sentiment += day_sentiment
            date_data.append([current_day,row["Close"],num_mentions])
            tickers[ticker].sentiment = sentiment
            tickers[ticker].mentions = total_mentions
            tickers[ticker].date_data = date_data
    return tickers


# gets the data for our current ticker, called in the above function
def get_comment_data(parsed_comments, ticker,current_day) -> list:
    day_sentiment = 0
    num_mentions = 0
    for comment in parsed_comments[ticker].comments: #iterate through all comments on that day
        if comment.date_posted == current_day:
            print("Found a mention of " + ticker)
            num_mentions += 1
            day_sentiment += comment.sentiment
    return (day_sentiment, num_mentions)


# this function reads the list of all the scraped comments, and find comments that mentioned a ticker.  it then calcualates the sentiment for that comment
def parse_comments(tickers, raw_comments, unix_time_frame) -> dict:
    
    parsed_comments = dict.fromkeys(tickers.keys(), Comments(unix_time_frame)) # copy keys from tickers dict into new dict, value at key is initally none

    for comment in raw_comments:# iterate through each word in the comment, 
        if comment.created_utc > unix_time_frame[0] and comment.created_utc < unix_time_frame[1]: # if the comment was posted within the time_frame argument
            for word in str(comment.body).split(" "): #.split() creates an array of words instead of iterating through charecters
                word = re.sub(r'\W+', '', word) # remove charecters that we dont need
                if word in tickers.keys():  # see if the currrent word is a valid ticker
                    # if so, create a comment object based on the current object
                    ticker = word
                    date_posted = datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d') # convert the unix timestamp to form (2021-01-04)
                    sentiment = get_sentiment(comment) # calculate sentiment for that comment
                    num_upvotes = comment.score
                    parsed_comments[ticker].comments.append(Comment(date_posted, num_upvotes, sentiment)) # add the comment to the comments array
                
    return parsed_comments

def get_sentiment(comment) -> float:
    cleaned_comment = re.sub(r'\W+', '', comment.body)
    analysis = TextBlob(cleaned_comment)
    return analysis.sentiment.polarity

def read_data(filename):
    data = pd.read_pickle(filename)

    for key in data.keys():

        cur = data[key]
        if(cur.mentions > 0):
            print("Ticker " + cur.ticker)
            print("full name: " + cur.full_name)
            print("sector : " + cur.sector)
            print("Number of mentions:" , cur.mentions)


def get_unix_time_frame(period):  #converts 1D, 1W, 1M, 1Y, 10Y to unix time ranges
    current_time = time.time()
    time_range = None
    if period == "1D":
        start_time = current_time - 86400
        time_range = [start_time,current_time]
    elif period == "1W":
        start_time = current_time - 604800
        time_range = [start_time,current_time]
    elif period == "1M":
        start_time = current_time - 2627999.9999716435559
        time_range = [start_time, current_time]
    elif period == "1Y":
        start_time = current_time - 31535965.4396976 
        time_range = [start_time, current_time]
    else:
        print("invalid period")
    return time_range

def get_plaintext_time_frame(unix_time_frame):
    return [datetime.fromtimestamp(unix_time_frame[0]).strftime('%Y-%m-%d'),datetime.fromtimestamp(unix_time_frame[1]).strftime('%Y-%m-%d') ]
    


if __name__ == "__main__":
    # take period and subreddit in from arguments

    period = sys.argv[1] # period from arguments ex "1Y"
    subreddit = sys.argv[2] #target subreddit ex "wallstreetbets"

    comment_file_name = scrape_reddit.scrape(subreddit,period) # scrape the comments, return the filename of the pkl that was created

    print("Comments have been scraped.  Building ticker objects...")

    unix_time_frame = get_unix_time_frame(period) # get unix timeframe from "1Y" by subtracting num of seconds from current epoch
    plain_text_time_frame = get_plaintext_time_frame(unix_time_frame)
    print(plain_text_time_frame)
    
    tickers = build_ticker_dict("../csv/tickers.txt", unix_time_frame) # build empty tickers

    raw_comments = pd.read_pickle(comment_file_name) #load our pickle file

    parsed_comments = parse_comments(tickers,raw_comments, unix_time_frame) # parsed the comments, putting into format described in functions

    tickers = get_date_data(tickers, plain_text_time_frame, parsed_comments) # fill ticker data
    print("Done!  Writing file...")

    filename = "done_" + comment_file_name
    outfile = open(filename, "wb") # save the pkl for the database
    pickle.dump(tickers, outfile) #
    
