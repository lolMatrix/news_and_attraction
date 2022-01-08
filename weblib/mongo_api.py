#!/usr/bin/env python
import json

import requests

import weblib


def get_news_list():
    return requests.get(weblib.url + "/news/").json()

def save_news(data: dict):
    jsn = json.dumps(data)
    return requests.post(weblib.url + "/news/save/", json=jsn).json()

def update_news(update: dict):
    return requests.put(weblib.url + "/news/update/", json=update)
