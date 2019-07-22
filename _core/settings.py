import os
import environ

env = environ.Env()
env.read_env('.env')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY', default='*do30%6&7ThD4bi7xka8cavt*sse!3ehdo@saiuh)6fo40gvos')

DEBUG = env.bool('DEBUG', default=False)

SITE_ID = 1

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

WEBPACK_DEV_SERVER = env('WEBPACK_DEV_SERVER', default='localhost:8080')

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

REST_FRAMEWORK = {
    'DATETIME_FORMAT': DATETIME_FORMAT
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SERP_SCRAPER_TIME_LIMIT = 300

DEFAULT_UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'serp',
    'csp',
    'rest_framework',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'spoof'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = '_core.urls'

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
            ],
        },
    },
]

# All auth
LOGIN_REDIRECT_URL = '/'
ACCOUNT_FORMS = {
    "login": "serp.forms.LoginForm"
}

WSGI_APPLICATION = '_core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='postgres'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASS', default='postgres'),
        'HOST': env('DB_HOST', default='db'),
        'PORT': env('DB_PORT', default=5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MET'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'dist')

# In debug mode serve files from webpack dev server for auto reloading
if DEBUG:
    STATIC_URL = env('STATIC_URL', default='http://{}/static/'.format(WEBPACK_DEV_SERVER,))
else:
    STATIC_URL = env('STATIC_URL', default='/static/')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Content Security Policy
CSP_DEFAULT_SRC = ("'self'", WEBPACK_DEV_SERVER, "'unsafe-inline'", "data:")
CSP_SCRIPT_SRC = ("'self'", "*", WEBPACK_DEV_SERVER, "'unsafe-inline'", "'unsafe-eval'")
CSP_STYLE_SRC = ("'self'", WEBPACK_DEV_SERVER, "'unsafe-inline'")
CSP_CONNECT_SRC = ("'self'", WEBPACK_DEV_SERVER, "ws:")
