# Import flask
from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
# Import the python scraping file (scrape_stock.py)
import scrape_stock
import os


# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable to MongoDB
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

# Set route to query mongoDB and make an HTML template
@app.route("/")
def home():
    # find and store the data in stock_info mongo db
    stock_info = mongo.db.stock_info.find_one()

    # Return the template with the stock info passed in
    return render_template("index.html", stock_info=stock_info)

# Create a route called /scrape
@app.route("/scrape")
def scrape():
    # execute scrape funcions
    stock_info = mongo.db.stock_info
    stock_data = scrape_stock.scrape_stock()
    

    # update mongo database
    stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
