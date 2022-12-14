"""
Django settings for xapi project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import datetime, timedelta
import django.http.request as request

LOCALHOST = os.environ.get('HOSTNAME')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.dirname(os.path.dirname('app-react'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l6ouy*ap*m#!*engwsw8kl2==utk!x9z(gw09cveec++u3tf=j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: don't run with 'TEST_LOCAL' turned on in production!
TEST_LOCAL = False

# SECURITY WARNING: don't run with 'USE_LOCAL_STORAGE' turned on in production!
USE_LOCAL_STORAGE = False

# SECURITY WARNING: don't run with INITIAL turned on in production!
# Set 'INITIAL' to "True" when making initial database creation makemigrations and migrate, then set to "False" before
# creating superusers/going any further and for the rest of the time the database exists.
INITIAL = False

"""~~!!!!!!!!~~ PLEASE DON'T ADJUST ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING ~~!!!!!!!!~~"""

if TEST_LOCAL:
    # Change to false if testing oauth2 on local.
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    CSRF_COOKIE_HTTPONLY = False
    X_FRAME_OPTIONS = 'DENY'

else:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_HTTPONLY = True
    X_FRAME_OPTIONS = 'DENY'

if USE_LOCAL_STORAGE:
    # if the local storage does not exist go ahead and create it,
    # replace the local storage with whatever directory you want if you're worred about space, or if my original spot
    # isn't good enough for you... its okay I understand, you just won't be invited to the next party... your move
    # make sure to update the relative path of the LOCAL_STORAGE_URL as well
    # for example:
    # LOCAL_STORAGE_LOCATION = os.path.join(BASE_DIR, "local_storage")
    # LOCAL_STORAGE_URL = '/local_storage/'

    LOCAL_STORAGE_LOCATION = os.path.join(os.path.join(os.path.join(BASE_DIR, "xui"), "public"), "local_storage")
    LOCAL_STORAGE_URL = '/local_storage/'
    if not os.path.isdir(LOCAL_STORAGE_LOCATION):
        os.makedirs(LOCAL_STORAGE_LOCATION)

else:
    LOCAL_STORAGE_LOCATION = None
    LOCAL_STORAGE_URL = None

ALLOWED_HOSTS = [
    '52.41.200.41',
    'app.xspaceapp.com',
    'api.xspaceapp.com',
    'dev-us1.xspaceapp.com',
    'dev-api.xspaceapp.com',
    '127.0.0.1',
    '172.16.0.31',
    '54.191.102.47',
    '52.10.110.128',
    '54.69.4.144',
    'localhost'
]

# Application definition
INSTALLED_APPS = [
    'app',
    'app.accounts',
    'app.products',
    'app.core',
    'app.orders',
    'django_extensions',
    'account',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'rest_framework_docs',
    'rest_framework.authtoken',
    'rest_framework_datatables',
    'oauth2_provider',
    'corsheaders',
    'postman',
    'sslserver',
    'webpack_loader',
    'drf_yasg',
    'notifications'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'xapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'xapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
if TEST_LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'xspaceapp',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

AUTHENTICATION_BACKENDS = (
    'account.auth_backends.EmailAuthenticationBackend',
    # Uncomment the following to make Django tests pass:
    'django.contrib.auth.backends.ModelBackend',
    'oauth2_provider.backends.OAuth2Backend',
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
    },

}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',

    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

X_FRAME_OPTIONS = 'ALLOW'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "core/static/"),
]

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = [
    'app.xspaceapp.com',
]

CORS_REPLACE_HTTPS_REFERER = True
CSRF_COOKIE_DOMAIN = 'xspaceapp.com'

###############
#   Postman   #
###############
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

POSTMAN_I18N_URLS = True
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_NAME_USER_AS = 'email'
POSTMAN_AUTOCOMPLETER_APP = {
    # 'name': '',  # default is 'ajax_select'
    # 'field': '',  # default is 'AutoCompleteField'
    # 'arg_name': '',  # default is 'channel'
    'arg_default': 'postman_users', }  # no default, mandatory to enable the feature
############
#   KEYS   #
############

AWS_ACCESS_KEY_ID = 'AKIAI5SSQDOJ2PH2AKIA'
AWS_SECRET_ACCESS_KEY = '7IGts/H9pDpLifref02T9DbSREqdq6SRx91CoZgx'
AWS_S3_REGION_NAME = 'us-west-2'  # e.g. us-east-2
AWS_STORAGE_BUCKET_NAME = 'storagev2'
AWS_S3_CUSTOM_DOMAIN = '%s.s3-us-west-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = 'False'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
CLOUDFRONT_DOMAIN = 'd27vruithpdhv2.cloudfront.net'
CLOUDFRONT_ID = 'EWR57JUETT9CX'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=0',
}

AWS_DEFAULT_ACL = 'public-read'

ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

AUTH_USER_MODEL = 'app.User'
AUTH_PROFILE_MODULE = "app.Profile"

# settings.py
IMAGE_SIZES = {
    'normal': {
        'size': (500, 0),
        'quality': 85
    },
    'tiny_square': {
        'size': (100, 100),
        'crop': True
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'no-reply@xspaceapp.com'
EMAIL_HOST_PASSWORD = 'Dampim2020!'
EMAIL_PORT = 587

# Security Settings
BUGSNAG = {
    'api_key': '6fa8e7eee66e02b02ce4eabfada3882d',
    'project_root': '/home/ubuntu/xspace-webapp-v2',
}

TEMPLATE_DIRS = (
    APP_DIR + '/templates/' + '',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-api-subdomain'
)

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://localhost:3000'
)

CORS_ORIGIN_ALLOW_ALL = True

SITE_ID = 2
DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True, 'SOFT_DELETE': True}

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
    },

    'CLIENT_ID_GENERATOR_CLASS': 'oauth2_provider.generators.ClientIdGenerator',

}

if not INITIAL:
    OAUTH2_PROVIDER_APPLICATION_MODEL = 'app.Application'

# BG_REMOVE_KEY = 'MT8CBfCA45c3EUNS3aCqiey9'
BG_REMOVE_KEY = 'sA1PpaBnrpK5jyEiutaqBpgc'

# if DEBUG:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             },
#         },
#     }
#
