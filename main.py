#!/usr/bin/env python

from web import manage
from threading import Thread
from caruler.kurs import spider
from tomitaworker import TomitaWorker

if __name__ == "__main__":
    thread = Thread(target=spider.start_spider, daemon=True)
    thread.start()
    threadTomita = Thread(target=TomitaWorker.run(), daemon=True)
    threadTomita.start()
    manage.runserver()
