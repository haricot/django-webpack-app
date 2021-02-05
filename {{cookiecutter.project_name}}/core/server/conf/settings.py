from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
with open(BASE_DIR / '.env') as env_file:
    env.read_env(env_file)

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
    CORS_ALLOW_ALL_ORIGINS = True
else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', cast=str)
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
{% if cookiecutter.use_redis == "No" -%}
    'django.contrib.sessions',
{%- endif %}
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'corsheaders',
    'django_extensions',
     rest_framework.authtoken',
    'rest_framework',
    'drf_yasg',
    'drf_registration',
    'server.app.ServerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'server' / 'templates'],
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

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }
}

{% if cookiecutter.use_redis == "Yes" -%}
REDIS_URI=env.str('REDIS_URI')

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URI}/{env.str('REDIS_DJANGO_CACHE_DB')}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
{%- endif %}

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

if DEBUG:
    default_permissions = ['rest_framework.permissions.AllowAny']
else:
    default_permissions = [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.authentication.SessionAuthentication',
    ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': default_permissions,
}
AUTHENTICATION_BACKENDS = [
    'drf_registration.auth.MultiFieldsModelBackend',
]

AUTH_USER_MODEL = 'server.User'

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'huychau.dev@gmail.com'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# DRF REGISTRATION configurations
DRF_REGISTRATION = {
    'USER_ACTIVATE_TOKEN_ENABLED': False,
    'REGISTER_SEND_WELCOME_EMAIL_ENABLED': False,
    'FACEBOOK_LOGIN_ENABLED': False,
    'GOOGLE_LOGIN_ENABLED': True,

    'LOGIN_USERNAME_FIELDS': ['email', 'username', 'first_name'],
}
import os
STATICFILES_DIRS = (BASE_DIR / 'dist',
  os.path.join(BASE_DIR , 'node_modules', 'bootstrap')
)


SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'server.urls.openapi_info',
}

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

dev_static = os.getenv('DJANGO_STATIC_ROOT')

if not dev_static:
    STATIC_ROOT = '/opt/static'
else:
    STATIC_ROOT = '../static'

# futur possible directly with webpack https://pascalw.me/blog/2020/04/19/webpack-django.html
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/bundle/',
        'STATS_FILE': BASE_DIR / 'webpack-stats.json',
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

LOGIN_URL = '/admin/login'
