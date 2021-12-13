# web_scrapping_challenge


Jupyter Note Book - 

NASA Mars News

Scrapes the Mars News Site and collects the latest News Title and Paragraph Text. 


Use splinter to navigate to the site and find the image url for the current Featured Mars Image.

Visits the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Uses Pandas to convert the data to a HTML table string.

Visits the astrogeology site to obtain high resolution images for each of Mar's hemispheres.


MongoDB and Flask Application - 

Uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped.


Starts by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all the scraping code.


Has route called /scrape that will import the scrape_mars.py script and calls the scrape function.

Stores and returns value in Mongo as a Python dictionary.

Has a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.


Uses template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.