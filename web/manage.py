#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from threading import Thread

from caruler.kurs import spider


def runserver():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.web.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    thread = Thread(target=spider.start)
    thread.start()

    execute_from_command_line(["", "runserver"])
