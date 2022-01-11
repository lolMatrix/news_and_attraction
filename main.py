#!/usr/bin/env python

from web import manage
from threading import Thread
from caruler.kurs import spider
from tomitaworker import tomita_worker

if __name__ == "__main__":
    thread = Thread(target=spider.start_spider, daemon=True)
    thread.start()

    threadTomita = Thread(target=tomita_worker.start_tomita, daemon=True)
    threadTomita.start()

    manage.runserver()
