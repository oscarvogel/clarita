"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ee1749c+j87^w%7#123d=dw0zm1q)_bn&txuv3k-pm04@8=@n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.ecommerce',
    'apps.account',
    'apps.cart',
    'import_export',
    'sorl.thumbnail',
    'apps.orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/


LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TITULO_PRINCIPAL = "Clarita Digital"
NOMBRE_SITIO = "Ventas"
WEB_EMPRESA = "http://www.superclarita.com.ar"
TELEFONO_EMPRESA = '+54 3743 667526'
EMAIL_EMPRESA = 'ventas@claritadigital.com.ar'
DOMICILIO_EMPRESA = 'Av. 9 de Julio - Pto Rico - Misiones'

LOGIN_REDIRECT_URL = reverse_lazy('cuenta:dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

CART_SESSION_ID = 'cart'

EMAIL_HOST = 'mail.ferreteriaavenida.com.ar'
EMAIL_PORT = 587
EMAIL_HOST_USER = "info@ferreteriaavenida.com.ar"
EMAIL_HOST_PASSWORD = "Fasa0298"
EMAIL_USE_TLS = False
ADMINS = [('Oscar Vogel', 'oscar@ferreteriaavenida.com.ar')]

REDIS_HOST = '192.168.0.200'
REDIS_PORT = 6379
REDIS_DB = 0
