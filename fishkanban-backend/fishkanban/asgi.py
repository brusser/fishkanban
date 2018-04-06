"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import sys
import django
from channels.routing import get_default_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'fishkanban.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fishkanban.settings")
django.setup()
application = get_default_application()