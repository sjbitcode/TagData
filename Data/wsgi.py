"""
WSGI config for Data project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'tags.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Data.settings")

application = get_wsgi_application()
