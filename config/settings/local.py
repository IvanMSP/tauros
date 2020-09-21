"""
    Local Settings
"""

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('NAMEDB'),
        'USER': config('USERDB'),
        'PASSWORD': config('PASSWORDDB'),
        'HOST': 'localhost',
        'PORT': ''
       },
   }

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
