# WEBSCRAOER https://realpython.com/beautiful-soup-web-scraper-python/

# INSTALL VIRTUAL ENVIRONMENT
#python3 -m venv venv
# ACTICVATE IT
#source venv/bin/activate
#(venv) $
# INSTALL PACKAGES INTO IT
#(venv) $ python3 -m pip install <package-name>
# DEACTIVATE IT
#(venv) $ deactivate
# FOLDER STRUCTURE
#sudo apt install tree
#tree venv
"""
bin/ contains the executable files of your virtual environment. 
Most notable are the Python interpreter (python) and the pip executable (pip), 
as well as their respective symlinks (python3, python3.10, pip3, pip3.10). 
The folder also contains activation scripts for your virtual environment. 
Your specific activation script depends on what shell you use. For example, 
in this tutorial, you ran activate, which works for the Bash and Zsh shells.
include/ is an initially empty folder that Python uses to include C header 
files for packages you might install that depend on C extensions.

lib/ contains the site-packages/ directory nested in a folder that designates 
the Python version (python3.10/). site-packages/ is one of the main reasons 
for creating your virtual environment. This folder is where you’ll install 
external packages that you want to use within your virtual environment. 
By default, your virtual environment comes preinstalled with two dependencies, 
pip and setuptools. You’ll learn more about them in a bit.

lib64/ in many Linux systems comes as a symlink to lib/ for compatibility 
reasons. Some Linux systems may use the distinction between lib/ and lib64/ 
to install different versions of libraries depending on their architecture.

pyvenv.cfg is a crucial file for your virtual environment. It contains only 
a couple of key-value pairs that Python uses to set variables in the sys 
module that determine which Python interpreter and which site-packages 
directory the current Python session will use. You’ll learn more about the 
settings in this file when you read about how a virtual environment works.

There are three essential parts of a Python virtual environment:
A copy or a symlink of the Python binary
A pyvenv.cfg file
A site-packages directory - are optional but come as a reasonable default
"""

# STATIC WEBSITES
import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
scrapeResults = open('scrapeResults', 'w+')
# print(page.text)
scrapeResults.write(page.text) # cat scrapeResults
scrapeResults.close()
"""
 requests-html is a project created by the author of the requests library 
 that allows you to render JavaScript using syntax that’s similar to the 
 syntax in requests. It also includes capabilities for parsing the data by 
 using Beautiful Soup under the hood.

 Note: Another popular choice for scraping dynamic content is Selenium. 
 You can think of Selenium as a slimmed-down browser that executes the
 JavaScript code for you before passing on the rendered HTML response to 
 your script.
"""

# PARSE HTML CODE WITH BEAUTIFUL SOUP - a Python library for parsing structured data.
# python3 -m pip install beautifulsoup4
# import library - from bs4 import BeautifulSoup
URL2 = 'https://realpython.github.io/fake-jobs/'
page2 = requests.get(URL2)
soup = BeautifulSoup(page2.content, 'html.parser')
scrapeResults2 = open('scrapeResults2', 'w+')
scrapeResults2.write(str(soup))
# print(soup)
scrapeResults2.close()
"""
Note: You’ll want to pass page.content instead of page.text to avoid problems 
with character encoding. The .content attribute holds raw bytes, which can be 
decoded better than the text representation you printed earlier using the 
.text attribute
The second argument, "html.parser", makes sure that you use the appropriate 
parser for HTML content.
"""

# FIND BY ELEMENT ID
elementId = soup.find(id='ResultsContainer')
# print(elementId.prettify())
scrapeElementId = open('scrapeElementId', 'w+')
scrapeElementId.write('FIND BY ELEMENT ID:\n' + elementId.prettify())
scrapeElementId.close()

# FIND BY HTML CLASS NAME
scrapeElementClass = open('scrapeElementClass', 'a')
scrapeElementClass.write('FIND BY HTML CLASS NAME:\n')
elementClass = elementId.find_all('div', class_='card-content')
for element in elementClass:
    scrapeElementClass.write(str(element) + '\n')
    # print(element, end='\n'*2)
    
# FIND BY DESCRIPTIVE CLASS NAME
scrapeElementClassByName = open('scrapeElementClassByName', 'w+')    
scrapeElementClassByName.write('FIND BY DESCRIPTIVE CLASS NAME:\n')
title_element = elementId.find('h2', class_='title')
company_element = elementId.find('h3', class_='company')
location_element = elementId.find('p', class_='location')
scrapeElementClassByName.write(str(title_element) + '\n')
scrapeElementClassByName.write(str(company_element) + '\n')
scrapeElementClassByName.write(str(location_element) + '\n')
"""
print(title_element)
print(company_element)
print(location_element)
"""

# EXTRACT TEXT FROM HTML 
scrapeElementClassByName.write('\nEXTRACT TEXT FROM HTML ELEMENTS:\n')
scrapeElementClassByName.write(str(title_element.text) + '\n')
scrapeElementClassByName.write(str(company_element.text) + '\n')
scrapeElementClassByName.write(str(location_element.text) + '\n')
"""
print(title_element.text.strip())
print(company_element.text)
print(location_element.text)
"""
  
# FIND BY CLASS NAME AND TEXT CONTENT DESPITE CAPITALIZATION
# pythonJobs = element.find_all('h2', string='Python') 
scrapeElementClassByName.write('\nFIND BY HTML CLASS NAME AND TEXT CONTENT DESPITE CAPITALIZATION:\n')
pythonJobs = elementId.find_all('h2', string=lambda text: 'python' in text.lower())   
scrapeElementClassByName.write(str(pythonJobs)+'\n'*2) 
scrapeElementClassByName.write('Python Jobs found: ' + str(len(pythonJobs)) + '\n')    
