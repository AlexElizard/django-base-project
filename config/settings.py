import environ
import re
from datetime import timedelta
from email.utils import getaddresses

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

BASE_DIR = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False))
env.read_env(str(BASE_DIR + '.env'))

##########################################################################################
#                                     BASE SETTINGS                                      #
##########################################################################################
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

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
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_HOSTS")
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

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

##################################
# Django Better Admin ArrayField #
##################################
INSTALLED_APPS.append('django_better_admin_arrayfield')

###################
# Django CKEditor #
###################
INSTALLED_APPS.extend([
    'ckeditor',
    'ckeditor_uploader',
])
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_UPLOAD_PATH = "ckeditor/"

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
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
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
#                             PROJECT APPLICATIONS SETTINGS                              #
##########################################################################################
INSTALLED_APPS += [

]

##########################################################################################
#                                    MODULES SETTINGS                                    #
##########################################################################################
##################
# AUTHENTICATION #
##################
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
AUTH_USER_MODEL = 'auth.User'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
]
if DEBUG:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append('rest_framework.authentication.SessionAuthentication')

############
# Database #
############
DATABASES = {
    'default': env.db(),
}
# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

############
# Datetime #
############
TIME_ZONE = 'Asia/Vladivostok'
USE_TZ = True

################
# File storage #
################
MEDIA_ROOT = BASE_DIR.path('media')
MEDIA_URL = '/upload/'
STATIC_ROOT = BASE_DIR.path('static')
STATIC_URL = '/django-static/'

########################
# Internationalization #
########################
LANGUAGE_CODE = 'ru'
USE_I18N = True
USE_L10N = True

###########
# Logging #
###########
ADMINS = getaddresses(env.list('ADMINS'))
MANAGERS = getaddresses(env.list('MANAGERS'))

LOG_FILES_DIR = BASE_DIR.path("tmp/logs/django")
EMAIL_FILE_PATH = BASE_DIR.path('tmp/mails')
SERVER_EMAIL = env.str('EMAIL_FROM')

IGNORABLE_404_URLS = [
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'standard': {
            'format': '[{levelname} | {asctime}] {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'filters': {
        'is_debug': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'is_not_debug': {
            '()': 'django.utils.log.RequireDebugFalse',
        },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['is_debug'],
            'formatter': 'standard',
        },
        'errors_to_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 10,
            'encoding': 'utf-8',
            'filename': f'{LOG_FILES_DIR}/errors.log',
            'filters': ['is_not_debug'],
            'formatter': 'standard',
        },
        'mail_to_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
            'filters': ['is_not_debug'],
            'include_html': True,
        }
    },
    'loggers': {
        'apps': {
            'level': 'DEBUG',
            'handlers': ['console', 'errors_to_file', 'mail_to_admins'],
            'propagate': False
        },
    }
}

###############
# SMTP server #
###############
DEFAULT_FROM_EMAIL = env.str('EMAIL_FROM')
EMAIL_CONFIG = env.email_url()
if EMAIL_CONFIG['EMAIL_BACKEND'] != environ.Env.EMAIL_SCHEMES['filemail']:
    del EMAIL_CONFIG['EMAIL_FILE_PATH']
vars().update(EMAIL_CONFIG)
