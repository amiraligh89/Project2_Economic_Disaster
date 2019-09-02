# Import flask
from flask import Flask, render_template, redirect, request
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
# Import the python scraping file (scrape_stock.py)
import hashtag
import os


print(__name__)
# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable to MongoDB
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

# Set route to query mongoDB and make an HTML template
@app.route("/")
def home():
    # find and store the data in stock_info mongo db
    # stock_info = mongo.db.stock_info.find_one()

    # Return the template with the stock info passed in
    #return render_template("index.html", stock_info=stock_info)
    return render_template("index.html", data=[])

# Create a route called /scrape
@app.route("/scrape")
def scrape():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info
    n = int(request.args.get('n'))
    search = request.args.get('search')
    data = hashtag.get_tweets(n, search)
    

    # update mongo database
    # stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return render_template("index.html", data=data)

#if __name__ == "__main__":
print("1...")
app.run(debug=True)
