import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

scrapeDynamicRequests = open('scrapeDynamicRequests', 'w+')
url = 'https://react-amazon-bestsellers-books-dy.netlify.app/'
session = HTMLSession()
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.find_all('article', class_='book'))  
response = session.get(url)
response.html.render()
# print(response.html)
# print(response.html.html) # THIS PROVIDES ALOT OF DATA SINCE IT IS DYNAMICALLY RENDERED
# print(response.html.find('article.book')) # WE CAN USE HTML.FIND BUT LET'S USE SOUP NOW:
soup = BeautifulSoup(response.html.html, 'html.parser')
# print(soup.find_all('article', class_='book')) # ALOT OF DATA
books = soup.find_all('article', class_='book')
scrapeDynamicRequests.write('DYNAMIC REQUESTS: ' + str(response.html) + '\n')
for book in books:
    print(book.find('h2').text)
    scrapeDynamicRequests.write(book.find('h2').text +'\n')
scrapeDynamicRequests.close()
