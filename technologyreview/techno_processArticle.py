import urllib.request

import requests
import xmltodict
from bs4 import BeautifulSoup
from . import models
import re




def findArticle():
    
    xmlFormat = getLatestXML()
    
    jsonFormat = (xmltodict.parse(xmlFormat))['rss']['channel']['item']

    jsonFormat = getUniqueArticle(jsonFormat)

    if jsonFormat is None:
        return 0,0,0,0

    url = jsonFormat['link']
    # print(url)
    
    # web_page = getArticleWebpage(url)
    # print(web_page)

    # if web_page is None:
    #     print('Webpage response from upstream server is empty')

    try:
        content = scrapArticle(url)
    except:
        return jsonFormat['title'], jsonFormat['description'], '', ''
    YTtitle = getYoutubeTitle(url)


    return jsonFormat['title'], jsonFormat['description'], content, YTtitle



def getUniqueArticle(jsonFormat):

    for item in jsonFormat:
        # print(len(getYoutubeTitle(item['guid']['#text'])))
        if len(getYoutubeTitle(item['link'])) <= 100:
            try:
                obj = models.Technodb.objects.get(title=item['title'])
            except models.Technodb.DoesNotExist:
                return item
    return None


def getLatestXML():
    req = urllib.request.Request(
    'https://hindi.gizbot.com/rss/gadgets-fb.xml',
    data=None, 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    }
    )

    return urllib.request.urlopen(req)

# def getArticleWebpage(url):
#     req = urllib.request.Request(
#     url,
#     data=None,
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
#     }
#     )
#     # print(req.type)
#
#     return urllib.request.urlopen(req)

def scrapArticle(web_page):
    r = requests.get(web_page)
    htmlcontent = r.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    content=soup.find_all('p')
    a=''
    for i in content:
        a=a+i.get_text()

    return a

def getYoutubeTitle(s):
    s = s.split('/')[-1]
    s = s.replace('-',' ')
    return str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0).capitalize(),s))