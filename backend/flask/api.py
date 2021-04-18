from flask import Flask, request
from flask_restful import Resource, Api
import pickle
import pandas as pd

class Ticker():  # ticker class, the dict is such that the key is a ticker and the value is a dict
    def __init__(self, ticker, full_name, sector):
        self.ticker = ticker  # ticker ex: TSLA
        self.full_name = full_name  # full name of the company
        self.sector = sector  # sector of the ticker
        self.comments = []  # list of comment objects provided by PRAW
        self.mentions = 0
        self.sentiment = []
        def getFullName(self):
            return (self.full_name)




app = Flask(__name__)
api = Api(app)

todos = {"AAPL" : [500, 3425345, 345345, 6988934, 34534], "TSLA" : [500, 3425345, 345345, 6988934, 34534], "F" : [500, 3425345, 345345, 6988934, 34534], "AMZN" : [500, 3425345, 345345, 6988934, 34534]}

        
x = pd.read_pickle("outwsb.pkl")

print(x["TSLA"].full_name)

class TodoSimple2(Resource):
    def get(self, ticker):
        return {ticker : x[ticker].getFullName()} 

class GetSorted(Resource):
    def get(self, sorted_by):
        if sorted_by == "hot":
            return {"hot" : [100]}
        elif sorted_by == "new":
            return {"new" : "newtest2"}

# class GetByTicker(Resource):
#     def get(self, ticker, timeframe):
#         if timeframe == "today":
#             return stocks_daily
#         if timeframe == "week":
#             return stocks_week[ticker]
#         elif timeframe == "month":
#             return stocks_monthly[ticker]
#         elif timeframe = ""

api.add_resource(TodoSimple2, '/<string:ticker>/')
api.add_resource(GetSorted, '/<string:sorted_by>/')

if __name__ == '__main__':
    app.run(debug=True)