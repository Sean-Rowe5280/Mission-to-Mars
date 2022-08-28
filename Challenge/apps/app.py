## Import Dependencies/Tools

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
# The second line says we'll use PyMongo to interact with our Mongo database.
# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.

## Set Up Flask

app = Flask(__name__)
app.debug = True
## Use flask_pymongo to set up mongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. 
# This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".
    # Why are we using URI in this task rather than URL?



## Define the route for the HTML page
    # Flask routes:
        # one for the main HTML page everyone will view when visiting the web app
        # one to actually scrape new data using the code we've written.

## Route for the HTML page

# This function links our visual representation of our work, our web app, to the code that powers it.

@app.route("/")      #  Tells Flask what to display when we're looking at the home page
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

    # index.html (index.html is the default HTML file that we'll use to display the content we've scraped). This means that when we visit our web app's HTML page, we will see the home page.
    # mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script. We will also assign that path to the mars variable for use later.
        # What is the find_one() method doing?
        # Why do we need to use the mongo=PyMongo(app) to find the mars collection?
    # return render_template("index.html" tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.
    # , mars=mars) tells Python to use the "mars" collection in MongoDB.

## Scraping Route

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars    
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

    # assign a new variable that points to our Mongo database: mars = mongo.db.mars.

    # we created a new variable to hold the newly scraped data: mars_data = scraping.scrape_all(). 
        # In this line, we're referencing the scrape_all function in the scraping.py file exported from Jupyter Notebook.

    # update the database using .update_one().
        # Here, we're inserting data, but not if an identical record already exists.
        # the query_parameter: .update_one(query_parameter, {"$set": data}, options) 
            # we can specify a field (e.g. {"news_title": "Mars Landing Successful"}), in which case MongoDB will update a document with a matching news_title.
            # Or it can be left empty ({}) to update the first matching document in the collection.
        # we'll use the data we have stored in mars_data
            # syntax used here is {"$set": data}. This means that the document will be modified ("$set") with the data in question.
        # upsert=True indicates to Mongo to create a new document if one doesn't already exist, and new data will always be saved (even if we haven't already created a document for it)

    # add a redirect after successfully scraping the data: return redirect('/', code=302).
        # his will navigate our page back to / where we can see the updated content.


if __name__ == "__main__":
    app.run()      

    #  final bit of code we need for Flask is to tell it to run

