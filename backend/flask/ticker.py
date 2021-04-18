class Ticker():  # ticker class, the dict is such that the key is a ticker and the value is a dict
    def __init__(self, ticker, full_name, sector):
        self.ticker = ticker  # ticker ex: TSLA
        self.full_name = full_name  # full name of the company
        self.sector = sector  # sector of the ticker
        self.comments = []  # list of comment objects provided by PRAW
        self.mentions = 0
        self.sentiment = []