import requests
import sys
from bs4 import BeautifulSoup
url = 'https://app.foursource.com/rfq/fabric'
r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content,'html5lib')

#print(r.content)

quotes = []
table = soup.find('div', attrs = {'id' : 'mf-header'})
print(table)