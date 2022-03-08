#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[2]:


# set your executable path, then set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Mars News

# In[3]:


# assign the url and instruct the browser to visit it
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# Notice how we've assigned slide_elem as the variable to look for the <div /> tag and its descendent (the other tags within the <div /> element)?
# This is our parent element. This means that this element holds all of the other elements within it, and we'll reference it when we want to filter


# In[5]:


# The specific data is in a <div /> with a class of 'content_title'.
slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url;  build the URL to the full-size image
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


# Create dataframe on details of Mars from galaxyfacts website
# "0" means to pull only first (index) table it encounters
df = pd.read_html('https://galaxyfacts-mars.com')[0]
# assign columns
df.columns=['description', 'Mars', 'Earth']
# turn description into the primary index
df.set_index('description', inplace=True)
# call dataframe
df


# In[14]:


# convert our DataFrame back into HTML-ready code
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[15]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[16]:


# 1. Use browser to visit the URL 
# url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
# adjusting to secondary site due to recent 503 error on above site.
url = 'https://marshemispheres.com/'
# Define base url variable
base_url = 'https://marshemispheres.com/'
browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[18]:


# 3. Write code to retrieve the image urls and titles for each hemisphere. 
    
# Parse the website
hemisphere_html = browser.html
hemisphere_soup = soup(hemisphere_html,'html.parser')

# identify code that contains url's and titles of the full size hemisphere images
hemisphere_img = hemisphere_soup.find_all('div', class_='description') 


# In[19]:


# create for loop for the multiple image urls and titles for each hemisphere.
for hemisphere_img in hemisphere_img:
    image_title = hemisphere_img.find('h3').get_text()
    
    # Find and visit the secondary html page
    image_url_secondary = f"{base_url}"+hemisphere_img.a['href']
    browser.visit(image_url_secondary)

    # Find the URL of the 'sample' link
    browser.is_element_present_by_text('sample', wait_time=1)
    image_url = browser.links.find_by_partial_text('Sample')['href'] 

    hemisphere_image_urls.append ({
        "img_url": image_url,
        "title":image_title})


# In[20]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

