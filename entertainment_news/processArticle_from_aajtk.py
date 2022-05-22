import urllib.request
import xmltodict
from bs4 import BeautifulSoup
# from . import models
import re
import urllib.request
from bs4 import BeautifulSoup

def dataFromThearticles():
    try:
        title = ""
        content = ""
        summary = ""
        YTtitle = ""
        urls = ""
        url = 'https://www.aajtak.in/entertainment/television'
        req = urllib.request.Request(
            url,
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        content = soup.find("div", {"class": "at_row"})
        content = content.find("div", {"class": "content-area"})
        content = content.find("div", {"class": "section-listing-LHS"})
        url_of_the_articles = content.find_all("div", {"class": "widget-listing"})
        for i in url_of_the_articles:
            url = i.find_all('a')
            urls = url[0]['href']
            break
        return articleContent(title,content,summary,YTtitle, urls,)
    except Exception as e:
        print(e)


def articleContent(title,content, description, YTtitle, urls):
    try:
        req = urllib.request.Request(
            urls,
            data=None,

            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
            }
        )
        data = urllib.request.urlopen(req)
        data = data.read()
        soup = BeautifulSoup(data, 'html.parser')
        articlePara = getArticlePara(soup)
        print('line 55')
        print(articlePara)
        print('line 57')
        articletitle = getArticleTitle(soup)
        print(articletitle)
        print('line 60')
        description = getArticleTitle(soup)
        print(description)
        print('line 63')
        Yttitle = YtTitle(urls)

        print(Yttitle)
        print('line 67')
        print(Yttitle)

        return articletitle,articlePara, description, Yttitle
    except Exception as e:
        print(e)


def getArticlePara(soup):
    try:
        content = soup.find_all("p")
        content_text = ""
        for i in content:
            content_text = content_text + " " + i.get_text()
        return content_text
    except Exception as e:
        print(e)



def getArticleTitle(soup):
    try:
        articletitle = soup.find_all("h1")
        for i in articletitle:
            articletitle = i.get_text()
            # print(articletitle)
            return articletitle
    except Exception as e:
        print(e)



def YtTitle(urls):
    try:
        # print(urls)
        s = urls.split('/')[-1]
        s = s.replace('-', ' ')
        s = s[:-23]
        return str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s))
    except Exception as e:
        print(e)



#-----------------------------------------
# ----------------------------------------


# dataFromThearticles()