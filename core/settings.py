from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv() 

SECRET_KEY = 'django-insecure-r$a5(on+pbsj#o2w@ni@&#%jdf)jq@()_-ht@*@3!@wax1rnwy'
DEBUG = True

# ------- COMMON CODE FOR HANDLE MEDA, STATIC and TEMPLATES ---------

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')

STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR , 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [STATIC_DIR, ]


MEDIA_DIR = os.path.join(BASE_DIR , 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


#  --------------------------==========-------------------------------

ALLOWED_HOSTS = ['fishbazar.pythonanywhere.com','www.fishbazar.pythonanywhere.com', '127.0.0.1', 'localhost','*']
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'adminpanel',
    'market',
    'django_filters',
    'payment',
    # 'rest_framework',
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

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# api/settings.py


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }

# dbname = os.environ.get('DBNAME')
# uname = os.environ.get('USERNAME')
# password = os.environ.get('PASSWORD')
# host = os.environ.get('HOST')
# port = os.environ.get('PORT')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': f'{dbname}',
#         'USER': f'{uname}',
#         'PASSWORD': f'{password}',
#         'HOST': f'{host}',
#         # 'PORT': f'{port}',
#     }
# }

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

# --=====> EXTRA <=====------


AUTH_USER_MODEL = 'users.User'
LOGIN_URL = "/auth/login/"
# ------======== ------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
