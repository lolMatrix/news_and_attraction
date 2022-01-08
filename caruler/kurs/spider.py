#!/usr/bin/env python

from weblib import mongo_api
from .crauler.HtmlParser import HtmlParser

parser = HtmlParser("http://www.volgograd.ru/news/")


def run():
    global news_list, parser
    for i in range(835):
        try:
            list = parser.parse_page(i + 1)
            add_list_in_db(list)
            print(f'{i + 1} страница добавлена')
        except Exception as e:
            print(f'технические шоколадки {e}')


def add_list_in_db(news):
    db_list = mongo_api.get_news_list()
    for item in news:
        if not is_equal_news(db_list, item):
            mongo_api.save_news(item)


def is_equal_news(newses_list, curr):
    for news in newses_list:
        if curr['title'] == news['title'] \
                and curr['date'] == news['date'] \
                and curr['link'] == news['link']:
            return True

    return False


def start_spider():
    while True:
        run()