from flask import Flask, render_template
import pymongo
#import insert_data
import scrape_mars

#Initialize flask app
app = Flask(__name__)

#set up Mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

@app.route("/")
def index():
    #Display the home page
    return render_template("index.html")

@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape_info()
    data = scrape_mars.scrape_info()
    print(data)
    #Display the home page
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)