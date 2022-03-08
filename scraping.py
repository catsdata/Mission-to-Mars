#import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# initialize browser, create data dictionary, end webdriver, return scraped data
def scrape_all():
    # Initiate headless driver for deployment
    # Had to temporarily enter in version number of the driver due to driver updating before chrome version
    executable_path = {'executable_path': ChromeDriverManager().install()}
    # headless true means we won't see it in action
    browser = Browser('chrome', **executable_path, headless=True)
    # set our news title and paragraph variables
    news_title, news_paragraph = mars_news(browser)

    # Create dictionary, run all scraping functions and store results in the dictionary
    # 2. create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image. 
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        # add hemispheres
        "hemisphere_image_urls": hemis(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

# 3. create a function that will scrape the hemisphere data by using your code from the Mission_to_Mars_Challenge.py file
def hemis(browser):
   
    # url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    url = 'https://marshemispheres.com/'
    # Define base url variable
    base_url = 'https://marshemispheres.com/'
    browser.visit(url)
    

    # Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Parse the website
    hemisphere_html = browser.html
    hemisphere_soup = soup(hemisphere_html,'html.parser')

    # identify code that contains url's and titles of the full size hemisphere images
    hemisphere_img = hemisphere_soup.find_all('div', class_='description') 

    
    # Write code to retrieve the image urls and titles for each hemisphere.
    for hemisphere_img in hemisphere_img:

        # Add try/except for error handling
        try:
            image_title = hemisphere_img.find('h3').get_text()
            
            # Find and visit the secondary html page
            image_url_secondary = f"{base_url}"+hemisphere_img.a['href']
            browser.visit(image_url_secondary)

            # Find the URL of the 'sample' link
            browser.is_element_present_by_text('sample', wait_time=1)
            image_url = browser.links.find_by_partial_text('Sample')['href'] 

            # append to the list
            hemisphere_image_urls.append({
                "img_url": image_url,
                "title": image_title})
        
        except AttributeError:
            return None, None

    return hemisphere_image_urls            

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())  