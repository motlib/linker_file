"""
Django settings for linker_file project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w0u!x*1sie503#xca!l0858%#1cmny-ye^p6dry@k$(wd63rx%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'lf_app.apps.LfAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lf_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'lf_project/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lf_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        # verbose log message formatter
        'verbose': {
            '()': 'colorlog.ColoredFormatter',
            'format': '[{asctime}] {log_color}{levelname:<8}{reset} {name}.{funcName}:{lineno} {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },

        # simple log message format, currently not in use
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    'handlers': {
        # log messages to console (stdout)
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },

        # Handler to log everything up to DEBUG level to file with log
        # rotation. Currently not in use, as docker container handles log data
        # written to console
        #'file': {
        #    'level': 'DEBUG',
        #    'class': 'logging.handlers.RotatingFileHandler',
        #    'filename': os.path.abspath(os.path.join(BASE_DIR, 'log', 'varweb.log')),
        #    'formatter': 'verbose',
        #    'maxBytes': 1024 * 1024 * 5, # 5 MB
        #    'backupCount': 5,
        #},
    },

    # root logger catches all log messages. Everything warning and above is sent
    # to the console and to the log file. Change the level e.g. to 'DEBUG' for
    # the development settings
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },

    # Loggers below the django hierarchy log to console with warning level, but
    # do not propagate to the root logger
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
            'propagate': False,
        },
    },
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
# where shall static files be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Additional directories that are searched for static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'lf_project/static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Authentication and Login / Logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'lf:index'
LOGOUT_REDIRECT_URL = 'lf:index'

# Select the template pack (framework) for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
