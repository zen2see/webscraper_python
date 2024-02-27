import requests
from bs4 import BeautifulSoup

scrapeXMLHTTPrequests = open('scrapeXMLHTTPrequests', 'w+')
headers = {
    'X-Requested-With': 'XMLHttpRequest'
}
url='https://librivox.org/advanced_search?title=&author=&reader=&keywords=&genre_id=0&status=all&project_type=either&recorded_language=&sort_order=alpha&search_page=1&search_form=advanced&q=The%20time%20machine'
response = requests.get(url, headers=headers)
data = response.json()
soup = BeautifulSoup(data['results'],'lxml')
book_titles = soup.select('h3 > a')
for item in book_titles:
    scrapeXMLHTTPrequests.write(item.text + '\n')
scrapeXMLHTTPrequests.close()