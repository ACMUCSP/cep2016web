import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = ['cs.ucsp.edu.pe']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cep2016',
        'USER': 'OVERWRITE',
        'PASSWORD': 'OVERWRITE',
    }
}

SECRET_KEY = 'OVERWRITE'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/cep2016/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR'
        }
    }
}
