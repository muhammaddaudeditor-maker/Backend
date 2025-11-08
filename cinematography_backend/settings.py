"""
Django settings for cinematography_backend project.
"""

import os
from pathlib import Path
import cloudinary
from cloudinary import uploader, api

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-here-change-this-later-12345'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost', '127.0.0.1', '*']

# -------------------------------------------------------------------
# Application definition
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    'cloudinary_storage',
    'cloudinary',
    'django_extensions',
    'django_filters',
    
    # Local apps
    'services',
    'portfolio',
    'about',
    'contact',
    'home',
    'project',
    'logo',
    'cv_upload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cinematography_backend.urls'

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

WSGI_APPLICATION = 'cinematography_backend.wsgi.application'

# -------------------------------------------------------------------
# Database (PostgreSQL on Neon) - HARDCODED
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_NvYTF4w9sUAm',
        'HOST': 'ep-muddy-flower-a1e5s9km-pooler.ap-southeast-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
        'CONN_MAX_AGE': 0,
    }
}

# -------------------------------------------------------------------
# Cloudinary Storage - HARDCODED
# -------------------------------------------------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dp1gkt6tp',
    'API_KEY': '542787591385464',
    'API_SECRET': 'WgzVxby9l4PdZPiXc26u2AkZlLI',
  
}

cloudinary.config( 
    cloud_name='dp1gkt6tp',
    api_key='542787591385464',
    api_secret='WgzVxby9l4PdZPiXc26u2AkZlLI',
    secure=True
    
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# -------------------------------------------------------------------
# Static Files
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Static Files (Fixed for Vercel)
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Only include STATICFILES_DIRS if the 'static' folder actually exists
# Otherwise comment it out or remove it
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Use WhiteNoise for static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------------------------------------------------
# Password Validation
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# Default primary key field type
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------------------
# CORS Settings
# -------------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# -------------------------------------------------------------------
# REST Framework
# -------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# -------------------------------------------------------------------
# Cache settings
# -------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}