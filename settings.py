import os
import yaml
with open('app_settings.yaml', 'r') as stream:
    SETTINGS = yaml.load(stream)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = SETTINGS['secret_key']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SETTINGS['db_name'],
        'USER': SETTINGS['db_user'],
        'PASSWORD': SETTINGS['db_pass'],
    }
}

if os.getenv('GAE_INSTANCE'):
    DEBUG = False
    DATABASES['default']['HOST'] = '/cloudsql/' + SETTINGS['cloudsql_connection']
    ALLOWED_HOSTS = ['.appspot.com']
    STATIC_URL = 'https://storage.googleapis.com/' + SETTINGS['bucket'] + '/static/'
else:
    DEBUG = True
    DATABASES['default']['HOST'] = SETTINGS['db_host_local']
    STATIC_URL = '/static/'
    ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'static/'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'somfy_controller.apps.SomfyControllerConfig',
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
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
