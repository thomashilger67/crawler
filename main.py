import time 
import requests 
from urllib.parse import urlparse 
from bs4 import BeautifulSoup
import urllib.robotparser


def mycrawler(url_start):

    def crawl(url):
        parsed_url=urlparse(url)
        

        robots_url=parsed_url.scheme + '://'+parsed_url.netloc + '/robots.txt'
        try :
            robots=requests.get(robots_url,timeout=20)
            '''
            allow=True
            if 'Disallow' in robots.text:
                for line in robots.text.splitlines():
                    if line =='Disallow: /':
                        allow=False 

            if allow:
                url_ouput.append(url)
            '''
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            rrate = rp.request_rate("*")

            if rp.can_fetch("*", url):
                url_ouput.append(url)

        except: 
            pass

    url_ouput=[]
    response=requests.get(url_start).content
    soup=BeautifulSoup(response,'html.parser')
    links=soup.find_all('a', href=True)

    links_url=[a['href'] for a in links]
    len_url=len(links_url)
    i=0
    while len(url_ouput)<50 and len_url>i+1:

        crawl(links_url[i])
        i+=1
        time.sleep(5)



    file = open('crawled_webpages.txt','w')
    for url in url_ouput:
        file.write(url+"\n")
    file.close()
    return url_ouput
                


if "__main__"==__name__:
    mycrawler("https://ensai.fr")