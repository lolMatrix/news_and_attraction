#!/usr/bin/env python
import requests as requests
from bs4 import BeautifulSoup
import lxml


class HtmlParser:
    def __init__(self, path):
        self.path = path

    def parse_page(self, page_number: int):
        newses_path = self.path + f"?PAGEN_1={page_number}"
        soup = self.get_html(newses_path)
        newses = soup.find_all("div", attrs={"class": "news-item"})

        news_list = []

        for news in newses:
            news_list.append(self.get_news(news))

        return news_list

    def get_html(self, url):
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'lxml')
        return soup

    def get_news(self, news):
        url = self.path.split('/news')[0] + news.h2.a['href']
        if isinstance(url, list):
            url = url[0]

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
        soup = self.get_html(url)
        text = soup.select_one("#full_text")

        full_text = ""
        if text is not None:
            paragraphs = text.find_all("p")
            for paragraph in paragraphs:
                full_text += paragraph.text

        return full_text
