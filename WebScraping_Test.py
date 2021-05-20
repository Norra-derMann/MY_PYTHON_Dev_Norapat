import requests
from bs4 import BeautifulSoup

#url = 'https://th.wikipedia.org/wiki/รายชื่อเทศบาลตำบลในประเทศไทย'
url = 'https://www.brainyquote.com/topics/motivational-quotes'
resp = requests.get(url)
#print(resp.content)


soup = BeautifulSoup(resp.content, 'html5lib')
table = soup.find('div',attrs={'id' : 'quotesList'})
#print(table)
#print(table.prettify())

print(type(table))