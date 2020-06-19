"""
Django settings for linker_file project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

# pylint:disable=wildcard-import,unused-import,unused-wildcard-import
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = (
    '*',
)

# Application definition

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

# for debug_toolbar, needs to contain IP addresses which can see the toolbar
INTERNAL_IPS = [
        # ...
        '127.0.0.1',
        # ...
]
