from crauler.HtmlParser import HtmlParser
from weblib import mongo_api

parser = HtmlParser("http://www.volgograd.ru/news")


def run():
    global news_list, parser

    try:
        list = parser.parseFirstPage()
        db_list = mongo_api.get_news_list()
        for item in list:
            if not is_equil_news(db_list, item):
                mongo_api.save_news(item)
                print("Добавлена новость")
    except:
        print('технические шоколадки')


def is_equil_news(newslist, curr):
    for news in newslist:
        if curr['title'] == news['title'] \
                and curr['date'] == news['date'] \
                and curr['link'] == news['link']:
            return True

    return False


while True:
    run()
