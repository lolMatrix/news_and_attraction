import array

import requests

import weblib


def get_news_list():
    return requests.get(weblib.url + "/news/").json()

def save_news(data: dict):
    return requests.post(weblib.url + "/news/save/", json=data).json()
