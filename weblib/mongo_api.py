#!/usr/bin/env python

import requests

import weblib


def get_news_list():
    return requests.get(weblib.url + "/news/").json()

def save_news(data: dict):
    return requests.post(weblib.url + "/news/save/", json=data).json()

def update_news(update: dict):
    return requests.put(weblib.url + "/news/update/", json=update)
