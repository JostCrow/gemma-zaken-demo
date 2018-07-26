"""
Django settings for zac project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from django.urls import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
BASE_DIR = os.path.abspath(os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'hijack',
    'compat',  # Part of hijack
    'hijack_admin',

    'zac.accounts',
    'zdsclient.contrib.django',

    # Demo applicaties
    'zac.demo.mor',
    'zac.demo.zaakbeheer',
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

ROOT_URLCONF = 'zac.urls'

# List of callables that know how to import templates from various sources.
RAW_TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'admin_tools.template_loaders.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DJANGO_PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': False,  # conflicts with explicity specifying the loaders
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'zac.demo.context_processors.settings',
            ],
            'loaders': RAW_TEMPLATE_LOADERS
        },
    },
]

WSGI_APPLICATION = 'zac.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Custom user model
AUTH_USER_MODEL = 'accounts.User'

# Logout redirect
LOGOUT_REDIRECT_URL = reverse_lazy('datamodel:index')

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(DJANGO_PROJECT_DIR, 'static'),
)

# Django-Hijack
HIJACK_LOGIN_REDIRECT_URL = '/'
HIJACK_LOGOUT_REDIRECT_URL = reverse_lazy('admin:accounts_user_changelist')
HIJACK_REGISTER_ADMIN = False
# This is a CSRF-security risk.
# See: http://django-hijack.readthedocs.io/en/latest/configuration/#allowing-get-method-for-hijack-views
HIJACK_ALLOW_GET_REQUESTS = True


#
# Project specific settings
#
# Add a Google API key to show a map in the demo application.
GOOGLE_API_KEY = ''

# ZDS Client configuration.
ZDSCLIENT_CONFIG = {
    'zrc': {
        'host': 'localhost',
        'port': 8000,
        'scheme': 'http'
    },

    'drc': {
        'host': 'localhost',
        'port': 8001,
        'scheme': 'http'
    },
    'ztc': {
        'host': 'localhost',
        'port': 8002,
        'scheme': 'http'
    },
    'orc': {
        'host': 'localhost',
        'port': 8003,
        'scheme': 'http'
    }
}

DEMO_BRONORGANISATIE = '517439943'

DEMO_ZTC_CATALOGUS_UUID = 'a0dfa894-0dd1-4395-8e8c-b169130d7ebb'
DEMO_MOR_ZTC_ZAAKTYPE_UUID = 'f82abbc7-e963-4808-961d-304cdde7f935'  # Melding Openbare Ruimte
DEMO_MOR_ZTC_STATUSTYPE_NEW_UUID = '9614ec19-ec65-4472-9a73-9f7f37c7c338'  # Nieuw

# Override settings with local settings.
try:
    from .local import *
except ImportError:
    pass
