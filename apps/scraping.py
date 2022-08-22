# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

## Define function to initialize the bowser, create data dictionary, end the WebDriver and return the scraped data.

def scrape_all():
    # Set up Splinter: Initialize headless driver for deployment

        ## we can see the word "browser" here twice: Coding guidelines do not require that these match, even though they do in our current code.
        ## one is the name of the variable passed into the function
        ## the other is the name of a parameter.

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)     ## Change headless=False to True, this runs scraping behind the scenes without the users seeing it.

    ## set our news title and paragraph variables 
    news_title, news_paragraph = mars_news(browser)    ## This line of code tells Python that we'll be using our mars_news function to pull this data.

    ## Run all scraping functions and store results in dictionary
        ## This has TWO things it does: (1)Runs all the functions we've creeated. (2)Stores all of the results.
        ## We'll need to create the HTML template: create paths to the dictionarys values allows us to present the data on our template.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()}      # Need to add the datetime import to our dependenciesas dt.

    # Stop webdriver and return data

    browser.quit()
    return data

## Define as Function-Scraping code for Title and Paragraph(Refractoring-10.5.2)
    ## Add argument to the function def mars_news(argmument)
            ## We'll be using the browser variable we defined outside the function. 
            ## All of our scraping code utilizes an automated browser, and without this section, our function wouldn't work.

def mars_news(browser):

### Red PLanet Articles scraping
    # Visit the Mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    ## Add try/except for error handling
        ## Address any potential errors that may occur during web scraping.
                ## AttributeErrors- The most common cause of an error is when the webpage's format has changed and the scraping code no longer matches the new HTML elements.


    try:

        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first a tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        ## news_title     ## Added to the function return. Removed from inside the function

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

        ## news_p         ## Added to the function return. Removed from inside the function

    except AttributeError:

        ## If there's an error, Python will continue to run the remainder of the code. 
        ## If it runs into an AttributeError, however, instead of returning the title and paragraph, Python will return nothing instead.

        return None, None    ## Two nones for each item we want returned in the function and included in the try/except.
        ## Return Statement

    return news_title, news_p

    # Instead of having our title and paragraph printed within the function, we want to return them from the function so they can be used outside of it.
    # adjust our code to do so by deleting news_title and news_p and include them in the return statement instead, as shown below.


### JPL Space Images Featured Image Scraping


## Define Function

def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    ## try/except for Attribute Errors
    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url

    ## Add Return Statement

    return img_url


### Mars Facts Scraping

## Add Define Function
def mars_facts():

## Add try/except
    try:
        ## Using Pandas' read_html() function to pull data, instead of scraping with BeautifulSoup and Splinter
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe

    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    ## Return/convert dataframe into HTML format, add bootstrap
    return df.to_html()

## Add script for flask: Code tells Flask that our script is complte and ready for action.(similiar to what was added to app.py)

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scraped_all())

##################################
# TO RUN: GO TO TERMINAL=>MAKE SURE CORRECT ENVIRONEMENT IS ACTIVATED=>SELECT THE CORRECT DIRECTORY WITH ls COMMAND=>TYPE python app.py INTO TERMINAL=>
