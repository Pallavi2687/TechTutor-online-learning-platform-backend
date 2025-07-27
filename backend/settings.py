from pathlib import Path
import os
from datetime import timedelta

# ───────────────
# Paths
# ───────────────
BASE_DIR = Path(__file__).resolve().parent.parent
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Where collected static files will be stored
# STATICFILES_DIRS = [
#     BASE_DIR / "static",  # Optional: Additional static file directories
# ]
# ───────────────
# Environment Variables
# ───────────────
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-default-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = [
    "localhost", 
    "127.0.0.1", 
    "techtutor-online-learning-platform-bx44.onrender.com"
]

DEBUG = True

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ───────────────
# Installed Apps
# ───────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    'cloudinary',
    'cloudinary_storage',

    "accounts",
    "courses",
    "enrollments",
    "reviews",
]

# ───────────────
# Middleware
# ───────────────
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ───────────────
# URL & WSGI
# ───────────────
ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

# ───────────────
# Templates
# ───────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# ───────────────
# Database (SQLite for development)
# ───────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ───────────────
# Password Validators
# ───────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ───────────────
# JWT Configuration
# ───────────────
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ───────────────
# CORS Configuration
# ───────────────
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",           # ✅ React dev frontend
    "https://your-frontend.vercel.app" # ✅ Deployed frontend (optional)
]
CSRF_TRUSTED_ORIGINS = [
    "https://techtutor-online-learning-platform-bx44.onrender.com",
    "http://localhost:3000",
]


# ───────────────
# REST Framework
# ───────────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# ───────────────
# Static & Media
# ───────────────
# STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ───────────────
# Custom User Model
# ───────────────
AUTH_USER_MODEL = "accounts.CustomUser"
# Media files with Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
import cloudinary

cloudinary.config(
    cloud_name="dsgdobp5f",
    api_key="319225148821162",
    api_secret="O0UNFetsamj60OzPBYuYuXwYXZ0"
)
