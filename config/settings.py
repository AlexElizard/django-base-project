import environ
import re
from datetime import timedelta
from email.utils import getaddresses

BASE_DIR = environ.Path(__file__) - 2
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
env = environ.Env(DEBUG=(bool, False))
env.read_env(str(BASE_DIR + '.env'))

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('DOMAINS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

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

##########################################################################################
#                                        PACKAGES                                        #
##########################################################################################
################
# CORS Headers #
################
if DEBUG:
    INSTALLED_APPS.append('corsheaders')
    MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
    CORS_ORIGIN_ALLOW_ALL = True

##################
# Django Filters #
##################
INSTALLED_APPS.append('django_filters')

#########################
# Django REST Framework #
#########################
INSTALLED_APPS.append('rest_framework')
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

#################
# Debug Toolbar #
#################
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
        'EXTRA_SIGNALS': [],
    }

###################
# DRF Spectacular #
###################
INSTALLED_APPS.append('drf_spectacular')
REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'

##############
# Simple JWT #
##############
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}

##########################################################################################
#                                        SETTINGS                                        #
##########################################################################################
##################
# AUTHENTICATION #
##################
AUTH_USER_MODEL = 'auth.User'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
]
if DEBUG:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
        'rest_framework.authentication.SessionAuthentication'
    )

############
# Database #
############
DATABASES = {
    'default': env.db(),
}

############
# Datetime #
############
USE_TZ = True
TIME_ZONE = 'Asia/Vladivostok'

################
# File storage #
################
STATIC_URL = '/django-static/'
STATIC_ROOT = BASE_DIR.path('static')
MEDIA_URL = '/upload/'
MEDIA_ROOT = BASE_DIR.path('media')

########################
# Internationalization #
########################
USE_I18N = True
LANGUAGE_CODE = 'ru'
USE_L10N = True

###########
# Logging #
###########
SERVER_EMAIL = env.str('EMAIL_FROM')
ADMINS = getaddresses(env.list('ADMINS'))
MANAGERS = getaddresses(env.list('MANAGERS'))
IGNORABLE_404_URLS = [
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

###############
# SMTP-server #
###############
DEFAULT_FROM_EMAIL = env.str('EMAIL_FROM')
EMAIL_CONFIG = env.email_url()
vars().update(EMAIL_CONFIG)
