# pip install selenium
# Download Chrome driver (appropriate version for your browser)

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

options = Options()
options.add_argument('--headless=new')

#  Set up Chrome Webdriver with Selenium by copying the path to your driver executable file
driver = webdriver.Chrome(options=options)

# Following that, navigate to the Google Search Page and provide your search keyword:
search_keyword = input('Enter a search keyword: ')
driver.get('https://google.com/search?q=' + search_keyword)

# Now you can simulate a continuous scroll. Using the script below
# Define the number of times to scroll
scroll_count = 5
for _ in range(scroll_count):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2) # Wait for results to load

# Use BeautifulSoup to parse and extract the results
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
search_results = soup.find_all('div', class_='tF2Cxc')
for result in search_results:
    title = result.h3.text
    link = result.a['href']
    print(f'Title: {title}')
    print(f'Link: {link}')
    print('\n')

# Close the WebDriver
driver.quit()
