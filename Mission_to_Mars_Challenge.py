# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# set your executable path, then set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

### Mars News

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# The specific data is in a <div /> with a class of 'content_title'.
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url;  build the URL to the full-size image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

### Mars Facts

# Create dataframe on details of Mars from galaxyfacts website
df = pd.read_html('https://galaxyfacts-mars.com')[0]
# assign columns
df.columns=['description', 'Mars', 'Earth']
# turn description into the primary index
df.set_index('description', inplace=True)
# convert our DataFrame back into HTML-ready code
df.to_html()

### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
browser.visit(url)

# Create a list to hold the images and titles.
hemisphere_image_urls = []

# Write code to retrieve the image urls and titles for each hemisphere; create for loop for the multiple images
for thumb in range(4):
    
    # Create dictionary & keys for images and titles
    hemisphere = {} 
    keys = range(2)
        
    # find the thumb element and click on it
    browser.find_by_tag("div.description a.itemLink.product-item")[thumb].click()
    
    # parse the new html page that opens
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # find the full image url and title
    img_url_rel = img_soup.select_one('li a').get('href')
    title = img_soup.select_one('h2', class_='title').get_text()
    
    # grab image URL & title variables for dictionary
    values = [img_url_rel, title]
    for i in keys:
        hemisphere[i] = values[i]
        
    # add image url and title to dictionary
    hemisphere['img_url'] = hemisphere.pop(0)
    hemisphere['title'] = hemisphere.pop(1)

    # append dictionary to main list
    hemisphere_image_urls.append(hemisphere)
    
    # Return to the first browser for next thumb
    browser.back()
