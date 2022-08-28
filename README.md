# Mission-to-Mars

## Project Overview

The Mission to Mars challenge was to scrape data about Mars from specific websites using Python and MongoDB and create a simple website to display the top news article, facts and images using Flask, HTML, and CSS.

## Results:
Utlizing these tools and putting it all together the final product is this simple yet effective webpage(Desktop Display:

![image](https://user-images.githubusercontent.com/107006216/187052330-0483637b-8238-4381-83e6-528b319dca97.png)
![image](https://user-images.githubusercontent.com/107006216/187054077-2780fa9c-f71d-4b0a-96d3-ea2087b4605b.png)

## The Challenge

- Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
  - In the scraping.py script we created a function called "hem_data" which navigates the sites pages using a for loop to locate the full image URL. The "scrape_all" function adds those URLs in a dictionary. The flask app is then called, it establishes a connection with MongoDB using flask_pymongo and upadates the database with the newly scraped data.
  
- Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
  - To update the webapp a section for "Mars Hemispheres" was added to the HTML.
  - This data was stored in MondgoDB as a list of dictionaries. In order to display the image and title for each hemisphere properly a for loop was added to the HTML
  - Additions to the HTML include:
  
  ![image](https://user-images.githubusercontent.com/107006216/187055693-ac06a894-6e8a-4d99-90a9-79e908adcb2a.png)

- Deliverable 3: Add Bootstrap 3 Components
  - 1. Use the Bootstrap 3 grid system to make the the website mobile-responsive.
      - The website was designed using .col-**__md__** so that it would be mobile responsive. On mobile devices, and tablets the columns will automatically stack for  easy viewing. See the below screenshot to see how it would be viewed on an iphone 12.
      
  - 2. Add two other Bootstrap 3 components.
      - The websie includes dozens of Bootstrap 3 compenents added to make the webpage more aesthetically pleasing. The facts table was customized, the primary styling for this was called within the scraping.py code. Additionally the background color,the styleing of "the Scrape New Data" button, and background header image we're all altered along with many other elements the HTML.
  
 
 Mobile-Responsive View:
  ![image](https://user-images.githubusercontent.com/107006216/187054417-84a2270d-6895-494a-87db-9f1954e09070.png)

  ![image](https://user-images.githubusercontent.com/107006216/187054305-c173aa2c-ccfc-4b1c-81b8-807ef70255c4.png)
  
  ![image](https://user-images.githubusercontent.com/107006216/187054356-dc6de19b-40a5-43a1-9732-870a81bff602.png)
  
  ![image](https://user-images.githubusercontent.com/107006216/187054406-aa29c033-194b-4dd3-829c-ff6aa4e1b4d0.png)

## Resources:

Websites:
- News: https://redplanetscience.com/
- Featured Image: https://spaceimages-mars.com
- Facts: https://galaxyfacts-mars.com'
- Hemisphere Images: https://marshemispheres.com/

Tools/Software:
- Python 3.7
- MondoDB 6.0
- Mongosh 1.5.4
- Flask 2.2.2
- HTML
- CSS
- Jupyter Notebook
- Visual Studio Code

Dependencies:
- splinter
- BeautifulSoup
- Pandas
- Webdriver_manager.chrome

