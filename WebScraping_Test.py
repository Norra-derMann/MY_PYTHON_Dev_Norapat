import requests

url = 'https://th.wikipedia.org/wiki/รายชื่อเทศบาลตำบลในประเทศไทย'
resp = requests.get(url)
print(resp.text)