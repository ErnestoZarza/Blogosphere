from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogosphere_db',
        'USER': 'postgres',
        'PASSWORD': 'passw0o0rd',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}


INTERNAL_IPS = ('10.10.3.2', '10.10.1.67', '192.168.218.128', '127.0.0.1', '0.0.0.0', 'localhost')
INSTALLED_APPS = ["debug_toolbar"] + INSTALLED_APPS
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/assets/jquery/jquery.min.js',
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}
