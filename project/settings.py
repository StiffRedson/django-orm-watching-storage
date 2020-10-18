import os

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", 'django.db.backends.postgresql_psycopg2'),
        'HOST': os.environ.get("SQL_HOST", 'checkpoint.devman.org'),
        'PORT': os.environ.get("SQL_PORT", '5434'),
        'NAME': os.environ.get("SQL_NAME", 'checkpoint'),
        'USER': os.environ.get("SQL_USER", 'guard'),
        'PASSWORD': os.environ.get("SQL_PASSWORD", 'osim5'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get("SECRET_KEY", default='REPLACE_ME')

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
