from dotenv import load_dotenv
import os


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv("SQL_ENGINE"),
        'HOST': os.getenv("SQL_HOST"),
        'PORT': os.getenv("SQL_PORT"),
        'NAME': os.getenv("SQL_NAME"),
        'USER': os.getenv("SQL_USER"),
        'PASSWORD': os.getenv("SQL_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=1))

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
