from pathlib import Path
import os

SECRET_KEY = 'django-insecure-r$a5(on+pbsj#o2w@ni@&#%jdf)jq@()_-ht@*@3!@wax1rnwy'
DEBUG = True

# ------- COMMON CODE FOR HANDLE MEDA, STATIC and TEMPLATES ---------

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = os.path.join(BASE_DIR , 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')
MEDIA_DIR = os.path.join(BASE_DIR , 'media')


STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [STATIC_DIR, ]

MEDIA_ROOT = MEDIA_DIR

#  --------------------------==========-------------------------------

ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost']
INSTALLED_APPS = [
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

# WSGI_APPLICATION = 'core.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# api/settings.py

WSGI_APPLICATION = 'core.wsgi.app'


# POSTGRES_URL="postgres://default:YGn4y5tmsSDo@ep-snowy-frog-a4ptwxad-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
# POSTGRES_PRISMA_URL="postgres://default:YGn4y5tmsSDo@ep-snowy-frog-a4ptwxad-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require&pgbouncer=true&connect_timeout=15"
# POSTGRES_URL_NO_SSL="postgres://default:YGn4y5tmsSDo@ep-snowy-frog-a4ptwxad-pooler.us-east-1.aws.neon.tech:5432/verceldb"
# POSTGRES_URL_NON_POOLING="postgres://default:YGn4y5tmsSDo@ep-snowy-frog-a4ptwxad.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
# POSTGRES_USER="default"
# POSTGRES_HOST="ep-snowy-frog-a4ptwxad-pooler.us-east-1.aws.neon.tech"
# POSTGRES_PASSWORD="YGn4y5tmsSDo"
# POSTGRES_DATABASE="verceldb"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',
        'USER': 'default',
        'PASSWORD': 'YGn4y5tmsSDo',
        'HOST': 'ep-snowy-frog-a4ptwxad-pooler.us-east-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': 
#         'HOST': '',
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
