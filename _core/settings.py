import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '*pz6w-p&%30!nbi7xka8cavt*sse!3ehdo@saiuh)6pyq^wglv'

DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

WEBPACK_DEV_SERVER = "localhost:8080"

REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S'
}

SERP_SCRAPER_TIME_LIMIT = 300

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
    'allauth.socialaccount'
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# All auth
LOGIN_REDIRECT_URL = '/'
ACCOUNT_FORMS = {
    "login": "serp.forms.LoginForm"
}

WSGI_APPLICATION = '_core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
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

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# In debug mode serve files from webpack dev server for auto reloading
if DEBUG:
    STATIC_URL = 'http://{}/static/'.format(WEBPACK_DEV_SERVER,)
else:
    STATIC_URL = '/static/'


# Content Security Policy

CSP_DEFAULT_SRC = ("'self'", WEBPACK_DEV_SERVER, "'unsafe-inline'", "data:")
CSP_SCRIPT_SRC = ("'self'", "*", WEBPACK_DEV_SERVER, "'unsafe-inline'", "'unsafe-eval'")
CSP_STYLE_SRC = ("'self'", WEBPACK_DEV_SERVER, "'unsafe-inline'")
CSP_CONNECT_SRC = ("'self'", WEBPACK_DEV_SERVER, "ws:")
