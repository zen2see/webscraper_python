# DYNAMIC WEBSITES USING CHROME AND SELENIUM
# https://chromedriver.chromium.org/downloads
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.69/win64/chromedriver-win64.zip
"""
Install Chrome. Install the most recent Google Chrome package on your PC.
sudo apt-get update
sudo apt-get install google-chrome-stable 
google-chrome -version

Next, go to the ChromeDriver download page and download chromedriver on your system.
wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.69/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip (not sure it worked had to install chromedriver-binary)
pip install chromedriver-binary
Now execute the below commands to configure ChromeDriver on your system.
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

Install selenium
pip install selenium
Download Required JAR files. To use Remote Selenium WebDrivers, you’ll need the Selenium Server.

"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
options = Options()
options.add_argument('--headless=new')

"""
FOR STATIC SITES:
response = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(response.text, 'lxml') 

FOR DYNAMIC SITES:"""
driver = webdriver.Chrome(options=options)
#service = Service(executable_path='/usr/bin/chromedriver')
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get('https://quotes.toscrape.com/js')
soup = BeautifulSoup(driver.page_source, 'lxml')
author_element = soup.find('small',class_='author')
print(author_element.text)
# Code to read data from html:
# quotes.toscrape.com
# element = driver.find_element_by_class_name('author')

#elements = driver.find_elements(by=By.CLASS_NAME, value='author')
#print(elements)
#for el in elements:
#    print(elements)

# element = driver.find_element('small') 
# element = driver.find_element('abc')
# element = driver.find_element('//abc')
# element = driver.find_elemebt('.abc')
driver.quit()