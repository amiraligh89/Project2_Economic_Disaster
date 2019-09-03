# Import flask
from flask import Flask, render_template, redirect, request

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo

# Import the python scraping files (scrape_stock.py, hashtag.py)
import scrape_stock
import hashtag

import os

print(__name__)
# Create an instance of our Flask app.
app = Flask(__name__)


# Set route to query mongoDB and make an HTML template
@app.route("/")
def home():
    # find and store the data in stock_info mongo db
    # stock_info = mongo.db.stock_info.find_one()

    # Create the empty templates for the stock and twitter scrapes
    return render_template("index.html", stock_info={}, data=[])

# Create a route called /scrape
@app.route("/scrape")
def scrape():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # stock scraping function
    stock_data = scrape_stock.scrape_stock()

    # twitter scraping function
    n = int(request.args.get('n'))
    search = request.args.get('search')
    data = hashtag.get_tweets(n, search)

    # update mongo database
    # stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return render_template("index.html", stock_info=stock_data, data=data)

#if __name__ == "__main__":
print("1...")
app.run(debug=True)