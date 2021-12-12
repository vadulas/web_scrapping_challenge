from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Initialize flask app
app = Flask(__name__)

#set up Mongo connection
mongo  = PyMongo(app, uri="mongodb://localhost:27017/Mars_DB")

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    #Display the home page
    print(f"======== {mars_data}")
    return render_template("index.html", data = mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    data = scrape_mars.scrape_info()
    print(data)

    # Insert into the Mongo database     
    mongo.db.collection.insert_one(data)
    # Redirect back to the home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)