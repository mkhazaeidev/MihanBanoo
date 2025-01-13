from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^282jc3-hdbtsh7+&wlw@7_xirj%%x@=ewvl&#8mkkkl&=0re2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['mihanbaanoo.com']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "extensions",
    "base.apps.BaseConfig",
    "accounts.apps.AccountsConfig",
    "preferences.apps.PreferencesConfig",
    "pages.apps.PagesConfig",
    "profiles.apps.ProfilesConfig",

    # Third Party Apps
    'phonenumber_field',
    'bootstrap5',
    'crispy_forms',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if not DEBUG:
    DATABASES["default"] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mihan_banoo_db',
        'USER': 'mihan_banoo_user',
        'PASSWORD': 'BSAB2202@MBDB',
        'HOST': 'localhost',
        'PORT': '5432',
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Bilingual settings
LANGUAGES = [
    ('en', _('English')),
    ('fa', _('Persian')),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = 'media/'

if DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_ROOT = BASE_DIR / 'media'
    STATICFILES_DIRS = [
        'base/static',
    ]
else:
    STATIC_ROOT = '/home/mihanbaanoocom/public_html/static/'
    MEDIA_ROOT = '/home/mihanbaanoocom/public_html/media/'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = 'pages:home'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django Crispy Forms
CRISPY_TEMPLATE_PACK = 'uni_form'
