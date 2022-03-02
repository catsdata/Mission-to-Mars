# Import tools
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection; connect to Mongo using a URI, a uniform resource identifier similar to a URL
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# create "Button" of the web application to run scraping
@app.route("/scrape")
def scrape(): 
   mars = mongo.db.mars #
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# run flask
if __name__ == "__main__":
   app.run()