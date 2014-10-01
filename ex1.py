from readability.readability import Document
import urllib
import lxml.etree
import lxml.html.clean

url = 'http://www.nfl.com/player/matthewstafford/79860/profile'
html = urllib.urlopen(url).read()

cleaner = lxml.html.clean.Cleaner()

readable_article = Document(html).summary().encode('utf-8')
print readable_article
readable_title = Document(html).short_title()

#print readable_article