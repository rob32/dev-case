# Project Name: DevCase
# Original Author: Robert Burkhardt
# License: GNU GPLv3
# Version: 1.2.2

import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(env_file):
    env.read_env(env_file)

SECRET_KEY = env.str("SECRET_KEY", default=get_random_secret_key())

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        "127.0.0.1",
        "localhost",
        "0.0.0.0",
    ],
)

DATABASE_URL = env.str("DATABASE_URL", default=False)

ADMIN_LOCATION = env.str("ADMIN_LOCATION", default="admin/")

ROBOTS_DISALLOW = env.list("ROBOTS_DISALLOW", default=None)

FEED_TITLE = env.str("FEED_TITLE", default="Articles")
FEED_DESCRIPTION = env.str("FEED_DESCRIPTION", default="Latest Articles")

USE_S3_STORAGE = env.bool("USE_S3_STORAGE", default=False)
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default="")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default="")
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default="")
AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL", default="")
AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", default="")
AWS_LOCATION = env.str("AWS_LOCATION", default="")
AWS_IS_GZIPPED = env.bool("AWS_IS_GZIPPED", default=False)
AWS_S3_FILE_OVERWRITE = env.bool("AWS_S3_FILE_OVERWRITE", default=True)
AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", default="public-read")

USE_UMAMI_ANALYTICS = env.bool("USE_UMAMI_ANALYTICS", default=False)
UMAMI_SCRIPT_URL = env.str("UMAMI_SCRIPT_URL", default="")
UMAMI_DATA_WEBSITE_ID = env.str("UMAMI_DATA_WEBSITE_ID", default="")

USE_PLAUSIBLE_ANALYTICS = env.bool("USE_PLAUSIBLE_ANALYTICS", default=False)
PLAUSIBLE_SCRIPT_URL = env.str("PLAUSIBLE_SCRIPT_URL", default="")
PLAUSIBLE_DATA_DOMAIN = env.str("PLAUSIBLE_DATA_DOMAIN", default="")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "solo",
    "captcha",
    "config",
    "blog",
    "portfolio",
    "contact",
    "pages",
]

SITE_ID = 1


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dev_case.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.main_settings",
                "pages.context_processors.pages_footer",
            ],
            "libraries": {
                "markdown_tags": "dev_case.templatetags.markdown_tags",
            },
        },
    },
]

# Append context_processors

if USE_UMAMI_ANALYTICS:
    TEMPLATES[0]["OPTIONS"]["context_processors"].append(
        "dev_case.context_processors.umami_analytics"
    )

if USE_PLAUSIBLE_ANALYTICS:
    TEMPLATES[0]["OPTIONS"]["context_processors"].append(
        "dev_case.context_processors.plausible_analytics"
    )


WSGI_APPLICATION = "dev_case.wsgi.application"


if DATABASE_URL:
    DATABASES = {"default": env.db()}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


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

USE_TZ = True


# Static files & Media

STATICFILES_DIRS = (str(BASE_DIR.joinpath("static")),)
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))

if USE_S3_STORAGE:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{STATIC_ROOT}/"
    MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{MEDIA_ROOT}/"

else:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    STATIC_URL = "static/"
    MEDIA_URL = "/media/"


# Settings for Local Development

if DEBUG:

    INSTALLED_APPS += [
        "django_extensions",
        "debug_toolbar",
    ]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
    ]

    # hack for Debug-Toolbar with docker
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]


# Enables security-settings for Production

SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False
)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)

SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=False)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=False)

# Settings for Django-Simple-Capctha

CAPTCHA_FONT_SIZE = 33
CAPTCHA_LETTER_ROTATION = (-15, 15)
CAPTCHA_NOISE_FUNCTIONS = ["captcha.helpers.noise_dots"]
CAPTCHA_LENGTH = 3

# Email Backend

USE_EMAIL_SMTP = env.bool("USE_EMAIL_SMTP", default=False)
EMAIL_NOTIFICATION = env.bool("EMAIL_NOTIFICATION", default=False)
EMAIL_RECIPIENT = env.str("EMAIL_RECIPIENT", default="")

DJANGO_ADMINS = env.list("DJANGO_ADMINS", default=None)

if DJANGO_ADMINS:
    ADMINS = [x.split(":") for x in DJANGO_ADMINS]

if USE_EMAIL_SMTP:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env.str("EMAIL_HOST", default="")
    EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
    EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
    EMAIL_PORT = env.int("EMAIL_PORT", default=587)
    DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="")
