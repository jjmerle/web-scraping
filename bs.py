import urllib
from bs4 import BeautifulSoup


url = 'http://en.wikipedia.org/wiki/University_of_Michigan'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

print(soup.title)
print(soup.title.string)