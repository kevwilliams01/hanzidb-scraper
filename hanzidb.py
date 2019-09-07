from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
num = 2
my_urls = ['http://hanzidb.org/character-list/by-frequency']
for url in range(1,100):
    url = 'http://hanzidb.org/character-list/by-frequency'+'?page='+str(num)
    my_urls.append(url)
    num+=1
for my_url in my_urls:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("tr")
    hanzi_temp = []
    for container in containers:
        hanzi_temp.append(container.td)
    hanzi1 = hanzi_temp[1:]
    hanzilist = []
    pinyin = []
    cnt = 0
    for x in hanzi1:
        hanzi = x.text
        hanzilist.append(hanzi)
    for tr in page_soup.findAll('tr'):
        td = tr.findAll('td')[1:2]
        if td:
            y = td[0].text
            pinyin.append(y)
    for z in range(1,101):
        print(hanzilist[cnt]+" "+pinyin[cnt])
        cnt+=1
