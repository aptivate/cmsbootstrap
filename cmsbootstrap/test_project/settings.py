# Django settings for  project.

# Build paths inside the project like this: path.join(BASE_DIR, ...)
from os import path
BASE_DIR = path.abspath(path.dirname(__file__))

import sys

########## DEFAULT DEBUG SETTINGS - OVERRIDE IN local_settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ASSETS_DEBUG = True
##########


########## DATABASES are configured in local_settings.py.*


########## SECRET CONFIGURATION
SECRET_KEY = 'zze11wwtq=o$lrx^afg(5@*40n6@=#jrgi0grj0rlybv_u^7s!'
DB_PASSWORD = 'vr52e3i3morx'
########## END SECRET CONFIGURATION


########## MANAGER/EMAIL CONFIGURATION
# These email addresses will get all the error email for the production server
# (and any other servers with DEBUG = False )
ADMINS = (
    ('Aptivate test_project team', 'test_project-team@aptivate.org'),
    ('Your Name', 'Your email'),  # this is in case the above email doesn't work
)

MANAGERS = ADMINS

# these are the settings for production. We can override in the various
# local_settings if we want to
DEFAULT_FROM_EMAIL = 'donotreply@Domain name'
SERVER_EMAIL = 'server@Domain name'
########## MANAGER/EMAIL CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/uploads/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = path.join(BASE_DIR, 'static')

# URL prefix for static files.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path.join(BASE_DIR, 'media'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_assets.finders.AssetsFinder',
)
########## END STATIC FILE CONFIGURATION

LOCALE_DIR = path.join(BASE_DIR, 'locale')
if path.isdir(LOCALE_DIR):
    LOCALE_PATHS = (LOCALE_DIR,)

########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'south', # Database migration helper
    'cms', # Django-CMS and its dependencies
    'mptt',
    'menus',
    'sekizai',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'django_assets',
    'cmsbootstrap',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # cms stuff
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    #
)
########## END MIDDLEWARE CONFIGURATION


########## URL Configuration
ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'wsgi.application'
########## END URL Configuration


########## django-secure - intended for sites that use SSL
SECURE = False
if SECURE:
    INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
########## end django-secure


########## AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    #"allauth.account.auth_backends.AuthenticationBackend",
)

# Some really nice defaults
#ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
########## END AUTHENTICATION CONFIGURATION


########## HAYSTACK SEARCH CONFIGURATION
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'test_project',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 1000
########## END HAYSTACK SEARCH CONFIGURATION
#

########## Custom user app defaults
# Select the correct user model
#AUTH_USER_MODEL = "users.User"
#LOGIN_REDIRECT_URL = "users:redirect"
########## END Custom user app defaults


########## SLUGLIFIER
#AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
########## END SLUGLIFIER


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## BINDER STUFF
# Usually included by adding intranet_binder as a git submodule
# The name of the class to use to run the test suite
# TEST_RUNNER = 'intranet_binder.testing.SmartTestSuiteRunner'

#MONKEY_PATCHES = ['intranet_binder.monkeypatches']
########## END BINDER STUFF

CMS_TEMPLATES = (
    ('custom/page_1col.html', 'Simple Page (no sidebars)'),
    ('custom/page_3col.html', 'Simple Page (both sidebars)'),
    ('custom/page_3col_notitle.html', 'Simple Page (without title, for plugins)'),
    ('custom/homepage.html', 'Home Page'),
    ('custom/placeholders_extra.html', 'Global Placeholders'),
)

# this section allows us to do a deep update of dictionaries
import collections
from copy import deepcopy


def update_recursive(dest, source):
    for k, v in source.iteritems():
        if dest.get(k, None) and isinstance(v, collections.Mapping):
            update_recursive(dest[k], source[k])
        else:
            dest[k] = deepcopy(source[k])


# used in admin template so we know which site we're looking at
DEPLOY_ENV = "localdev"
DEPLOY_ENV_NAME = "Local dev copy"
DEPLOY_ENV_COLOR = '#ff9900'  # orange

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': path.join(BASE_DIR, 'test_project.sqlite'), # Or path to database file if using sqlite3.
        'USER': 'test_project',                      # Not used with sqlite3.
        'PASSWORD': DB_PASSWORD,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST = 'localhost'

# turn off caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

#EXTRA_INSTALLED_APPS = ('debug_toolbar',)
#EXTRA_MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

# test stuff
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )


#CELERY_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



##### from here on is stuff that depends on the value of DEBUG
##### which is set in LOCAL_SETTINGS


if DEBUG is False:
    ########## SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    #ALLOWED_HOSTS = ["*"]
    ALLOWED_HOSTS = [
        '.Domain name',
        'www.Domain name',
        'fen-vz-test_project-stage.fen.aptivate.org',
        'fen-vz-test_project-dev.fen.aptivate.org',
        'test_project.dev.aptivate.org',
        'test_project.stage.aptivate.org',
    ]
    ########## END SITE CONFIGURATION

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # Your stuff: custom template context processers go here
    # cms stuff
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    #
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'templates'),
)

if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
########## END TEMPLATE CONFIGURATION


########## Your stuff: Below this line define 3rd party libary settings
