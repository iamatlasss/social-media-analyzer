"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from decouple import config, AutoConfig

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = ['*', 'localhost']

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3-rd party
    'django_celery_beat',
    'crispy_forms',
    'debug_toolbar',

    # local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'telegram.apps.TelegramConfig',
    'dashboard.apps.DashboardConfig',
    'db.apps.DBConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # debug in production
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'core.urls'
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
                'core.context_processors.full_user',
                'core.context_processors.current_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DB_NAME = config('DJANGO_DB_NAME')
DB_USER = config('DJANGO_DB_USER')
DB_PASSWORD = config('DJANGO_DB_PASSWORD')
DB_HOST = config('DJANGO_DB_HOST')
DB_PORT = config('DJANGO_DB_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'

#####################################################
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000000

# added settings
AUTH_USER_MODEL = 'users.SiteUser'

LOGIN_REDIRECT_URL = 'dashboard:main'
LOGOUT_REDIRECT_URL = 'pages:home'

# todo: move this vars to env vars for security reasons
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files')
MEDIA_URL = '/media/'

# Extra places for `collectstatic` to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_RESULT_BACKEND = 'amqp://localhost' # todo remove this url and add it to env vars
CELERY_RESULT_BACKEND = config('DJANGO_CELERY_RESULT_BACKEND')

# Celery Data Format
CELERY_ACCEPT_CONTENT = ['pickle', 'application/x-python-serialize', 'json']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_CREATE_MISSING_QUEUES = True
CELERY_RESULT_EXPIRES = 3600
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

from kombu.serialization import registry

registry.enable('json')
registry.enable('application/text')
registry.enable('application/x-python-serialize')

# task_routes = {
#     'path.to.the.new_task': {
#         'queue': 'tg_queue',
#         'routing_key': 'tg_queue',
#     },
#     'path.to.the.slow_task': {
#         'queue': 'slow_queue',
#         'routing_key': 'slow_queue'
#     }
# }

# task_annotations = {
#     'telegram.tasks.get_me': {'rate_limit': '5/m'}
#     '*': {'rate_limit': '2/m'}
# }
#####################################################
