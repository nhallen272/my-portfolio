"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/nate1/myblog')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/nate1/myblog/venv/lib/python3.8/site-packages')

# poiting to the project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
