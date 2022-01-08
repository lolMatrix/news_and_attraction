#!/usr/bin/env python

from web import manage
from threading import Thread
from caruler.kurs import spider

if __name__ == "__main__":
    thread = Thread(target=spider.start_spider, daemon=True)
    thread.start()
    manage.runserver()
