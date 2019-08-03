# Python BeautifulSoup web scraping libraries needed for extracting data.
#  extract URLs from one webpage.

from bs4 import BeautifulSoup
import requests

url ='http://hawlati.co'
reqeust_text= requests.get(url)

extracted = reqeust_text.text

print(extracted)
data=BeautifulSoup(extracted, ' html.parser')

link_tag= data.find_all('a')
for tag in link_tag:
      print(tag.get('herf'))
      
      


