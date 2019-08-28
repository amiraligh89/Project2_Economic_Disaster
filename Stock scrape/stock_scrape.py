# Dependenceis
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# MAC user: 
#https://splinter.readthedocs.io/en/latest/drivers/chrome.html
#!which chromedriver
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path, headless=False)

# Initialize browser
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Create a dictionary to store all scraped data
fed_info = {}

# Scraping function that exectutes the scraping of targeted webpages
def scrape_stocks():
    browser = init_browser()
    # Identifying the website to be scrapped and establishing a connection
    url_stocks = 'https://www.google.com/search?q=finance&rlz=1C5CHFA_enUS840US848&oq=S%26P+live+ticker&aqs=chrome.0.0.6151j1j8&sourceid=chrome&ie=UTF-8&stick=H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_lAQCCiJIYKAAAAA&tbm=fin&sa=X&ved=2ahUKEwjV7I6v65bkAhVnUd8KHSwCBZgQ6M8CMAB6BAgPEAI'
    browser.visit(url_stocks)
    time.sleep(1)

    # Creating a beautifulsoup object and parsing this object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting the exchange names, trading volumes, changes
    # tickers = soup.find_all('div', id = "kp-wp-tab-MARKET_SUMMARY")
    long_names = soup.find_all('span', class_ = "z4Fov")
    shares_traded = soup.find_all('span', class_ = "Z90tFb")
    changes = soup.find_all('span', class_ = "hO8Bcf")

    # Selecting the the targeted elements
    print(long_names[0].text, shares_traded[0].text, changes[0].text)
    print(long_names[1].text, shares_traded[1].text, changes[1].text)
    print(long_names[5].text, shares_traded[5].text, changes[5].text)
    print(long_names[6].text, shares_traded[6].text, changes[6].text)
    
    # how to store in list?

# def scrape_twitter():
#     browser = init_browser()
#     # Identifying the website to be scrapped and establishing a connection
#     url_twitter = 'https://www.google.com/search?q=finance&rlz=1C5CHFA_enUS840US848&oq=S%26P+live+ticker&aqs=chrome.0.0.6151j1j8&sourceid=chrome&ie=UTF-8&stick=H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_lAQCCiJIYKAAAAA&tbm=fin&sa=X&ved=2ahUKEwjV7I6v65bkAhVnUd8KHSwCBZgQ6M8CMAB6BAgPEAI'
#     browser.visit(url_twitter)
#     time.sleep(1)

#     # Creating a beautifulsoup object and parsing this object
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     # Extracting the exchange names, trading volumes, changes
    


    
#     #tweet = soup.find('div', class_='js-tweet-text-container')
#     #tweet = soup.find('p', class_='TweetTextSize').text
#     tweets = soup.find_all('div', class_='js-tweet-text-container')
#     for tweet in tweets:
#         fedbalances = tweet.find('a')
#         if "Insight" and "pressure" and "sol" in weather:
#             #print(fedbalances)
#             break
#         else:
#             pass

#     # Store data in mars_scraped_dict
#     fed_info['Fed Balances'] = fedbalances


