import requests
from bs4 import BeautifulSoup

url = requests.get('https://en.wikipedia.org/wiki/Deep_learning')
page = BeautifulSoup(url.content, 'html.parser')

print(page.title.string)

file = open('links.txt', 'w')

# Iterate and write all links with href attribute in txt file
for links in page.find_all('a'):
    file.write(str(links.get('href')) + '\n')

file.close()
