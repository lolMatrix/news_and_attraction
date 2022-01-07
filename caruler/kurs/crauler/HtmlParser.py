#!/usr/bin/env python
import requests as requests
from bs4 import BeautifulSoup
import lxml


class HtmlParser:
    def __init__(self, path):
        self.path = path

    def parseFirstPage(self):
        soup = self.gethtml(self.path)
        newses = soup.find_all("div", attrs={"class": "news-item"})

        news_list = []

        for news in newses:
            news_list.append(self.get_news(news))

        return news_list

    def gethtml(self, url):
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'lxml')
        return soup

    def get_news(self, news):
        url = self.path.split('/news')[0] + news.h2.a['href']
        text = news.select_one('.desc')
        if text.p is not None:
            text = text.p.text
        else:
            text = text.text

        text += self.get_full_text(url)

        result = {
            'date': news.find("div", attrs={"class": "date"}).text,
            'title': news.h2.a.text,
            'link': url,
            'text': text
        }
        return result

    def get_full_text(self, url):
        soup = self.gethtml(url)
        text = soup.select_one("#full_text")

        full_text = ""
        paragraphs = text.find_all("p")
        for paragraph in paragraphs:
            full_text += paragraph.text

        return full_text
