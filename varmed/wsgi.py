"""
WSGI config for varmed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

The settings file can be overridden by setting the env variable.
"""

import os
import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'varmed.settings.settings')

try:
    application = get_wsgi_application()
    print('[wsgi] without exception')
except RuntimeError:  # "populate() isn't reentrant"
    print('[wsgi] handling WSGI exception')
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
