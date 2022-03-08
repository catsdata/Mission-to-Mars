# Mission to Mars

<details><summary>Table of Contents</summary>
<p>

1. [Overview](https://github.com/catsdata/Mission-to-Mars#overview)
2. [Resources](https://github.com/catsdata/Mission-to-Mars#resources)
3. [Results](https://github.com/catsdata/Mission-to-Mars#results)
4. [Summary](https://github.com/catsdata/Mission-to-Mars#summary)

</p>
</details>

## Overview

## Resources

- Data Sources: 
    - [name](link)
- Software:  
    - Jupyter Notebook 6.4.6
    - SQLAlchemy 1.4.27
    - Python 3.7.11 with dependencies: 
        - pandas 1.3.5
        - numpy 1.20.3
    - *ADD MORE HERE*      

## Results

- Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles       
    - Code is written that retrieves the full-resolution image and title for each hemisphere image (10 pt)
    - The full-resolution images of the hemispheres are added to the dictionary. (10 pt)
    - The titles for the hemisphere images are added to the dictionary. (10 pt)
    - The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image. (10 pt)

- Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
    - The scraping.py file contains code that retrieves the full-resolution image URL and title for each hemisphere image (10 pt)
    - The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image (10 pt)
    - The index.html file contains code that will display the full-resolution image URL and title for each hemisphere image (10 pt)
    - After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images (10 pt)

![screencap](https://github.com/catsdata/Mission-to-Mars/blob/main/primary.png)

- Deliverable 3: Add Bootstrap 3 Components
    - The webpage is mobile-responsive (10 pt)
    - Two additional Bootstrap 3 components are used to style the webpage (10 pt)

![bootstrap](https://github.com/catsdata/Mission-to-Mars/blob/main/bootstrap_changes.png)

## Summary

Upload the following to your 'Mission-to-Mars' GitHub repository:
- The Mission_to_Mars_Challenge.ipynb file with all the code used for scraping.
- An updated scraping.py file.
- The app.py file.
- The index.html file in the template folder and any CSS stylesheets.
- A README.md that describes the purpose of the repository. Although there is no graded written analysis for this challenge, it is encouraged and good practice to add a brief description of your project.
