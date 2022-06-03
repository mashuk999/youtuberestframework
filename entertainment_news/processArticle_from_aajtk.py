import urllib.request
import xmltodict
from bs4 import BeautifulSoup
from . import models
import re
import urllib.request
from bs4 import BeautifulSoup


def dataFromThearticles():
    try:
        title = ""
        content = ""
        summary = ""
        YTtitle = ""
        unique_url = ""
        url_list = []
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
            url_list.append(urls)
            # print(url_list)
            unique_url = getUniqueArticle(url_list)
        return articleContent(title,content,summary,YTtitle, unique_url)
    except Exception as e:
        print(e)


def articleContent(title,content, description, YTtitle, urls):
    try:
        print(urls)
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
        # print('line 55')
        # print(articlePara)
        # print('line 57')
        articletitle = getArticleTitle(soup)
        # print(articletitle)
        # print('line 60')
        description = getArticleTitle(soup)
        # print(description)
        # print('line 63')
        Yttitle = YtTitle(urls)

        # print(Yttitle)
        # print('line 67')
        # print(Yttitle)

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
        s = s.split('tmov')
        yttitle = str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s[0]))
        return yttitle
    except Exception as e:
        print(e)



def getUniqueArticle(urls):
    for url in urls:
        try:
            s = url.split('/')[-1]
            s = s.replace('-', ' ')
            s = s.split('tmov')
            title_from_url = str(re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), s[0]))
            obj = models.entertainmentSaveVideonews_for_aajtk.objects.get(title=title_from_url)
            print('line 124')
            print(obj)
            print('line 126')
        except models.entertainmentSaveVideonews_for_aajtk.DoesNotExist:
            return url










#-----------------------------------------
# ----------------------------------------









dataFromThearticles()