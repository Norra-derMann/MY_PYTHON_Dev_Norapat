import requests
import sys
from bs4 import BeautifulSoup
import  csv
url = 'https://www.brainyquote.com/topics/motivational-quotes'
r = requests.get(url)

print(r.content)

if(r.status_code == 404):
    print('error Pls check your link')
else:
    print('website can access')

soup = BeautifulSoup(r.content, 'html5lib')
quotes = [] #list
table = soup.find('div',attrs={'id' : 'quotesList'}) #store html which div id = quotesList

for row in table.findAll('div', attrs = {'class' : 'qti-listm'}) : 
    quote = {} #dictionary
    try:
        quote['author'] = row.img['alt'].split("-")[1]
        quote['text'] = row.img['alt'].split("-")[0]
        quotes.append(quote)
        print(quote) #change quote to be list of dictionary
    except TypeError:
        continue
filename = 'short_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['author','text'])
    w.writeheader()
    for quote in quotes: #dictionary loop in list
        w.writerow(quote)

        #refernce tutorial : https://brightdata.com/blog/how-tos/how-to-use-beautiful-soup-for-web-scraping-with-python?cam=aw_blog_Beautiful-Soup-web-scraping_beautifulsoup%20python_520132069176&utm_term=beautifulsoup%20python&utm_campaign=blog&utm_source=adwords&utm_medium=ppc&utm_content=Beautiful-Soup-web-scraping&hsa_acc=1046276282&hsa_cam=13023430270&hsa_grp=124902841831&hsa_ad=520132069176&hsa_src=g&hsa_tgt=kwd-421857009773&hsa_kw=beautifulsoup%20python&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwy42FBhB2EiwAJY0yQh8PTGbcD13M5_UchLwbqPw_4dhUFnBdHp_k2q8lWNUUvzkXHwk_yhoCwGMQAvD_BwE
        
        #reference 2