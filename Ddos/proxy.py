import requests
import json
from bs4 import BeautifulSoup
from random import randint

request_Proxies = [] 
pr = requests.get("http://pubproxy.com/api/proxy?type=http&https=true&limit=2&level=anonymous")
proxie = json.loads(pr.text)
for proxyes in proxie['data']:
    request_Proxies.append({
       "http":"http://{}".format(proxyes['ipPort'])
        })

# print(request_Proxies)

# r = requests.get('https://sibidharan.me')
i=0
while i<5:
    pro = request_Proxies[randint(0,1)]
    i+=1
    print(pro)
    r = requests.get('http://localhost',proxies=pro)
    print(r.status_code)
    
# soup = BeautifulSoup(r.text,features="lxml")
# links ={}
# data = soup.findAll('a')
# print(data)
