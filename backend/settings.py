"""
Django settings for backend project.
Configurado para funcionar localmente (MySQL) y en Render (PostgreSQL).
"""

from pathlib import Path
import os
import dj_database_url
import mimetypes

BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# CONFIGURACIÓN GENERAL
# ===========================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temporal')

DEBUG = 'RENDER' not in os.environ  # Render define RENDER en entorno prod
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# CSRF confianza desde Render
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://sistema-cursos-frontend.onrender.com',
]

# ===========================
# APLICACIONES
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'corsheaders',

    # Locales
    'cursos',
]

# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # debe ir antes de CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # servir estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# CORS
# ===========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://sistema-cursos-frontend.onrender.com"
]
CORS_ALLOW_CREDENTIALS = True

# ===========================
# URLS Y WSGI
# ===========================
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# ===========================
# BASE DE DATOS
# ===========================
if os.environ.get('RENDER'):  # entorno Render (PostgreSQL)
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get(
                'DATABASE_URL',
                'postgresql://foro_db_r21o_user:oeAV5tDv3n54rYCQEIxwR2GomCPHwiQC@dpg-d3lulmt6ubrc73edka50-a.oregon-postgres.render.com/foro_db_r21o'
            ),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:  # entorno local (MySQL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sistema_cursos_db',
            'USER': 'sc_user',
            'PASSWORD': 'SCpassword123!',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }

# ===========================
# VALIDADORES DE CONTRASEÑAS
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================
# LOCALIZACIÓN
# ===========================
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ===========================
# ARCHIVOS ESTÁTICOS Y MEDIA
# ===========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Importante: permitir que Render sirva imágenes (solo mientras el contenedor viva)
if not DEBUG:
    # Render no guarda los archivos, pero esto permite servirlos temporalmente
    STATICFILES_DIRS = []
    mimetypes.add_type("image/svg+xml", ".svg", True)
    mimetypes.add_type("image/png", ".png", True)
    mimetypes.add_type("image/jpeg", ".jpg", True)
    mimetypes.add_type("image/jpeg", ".jpeg", True)

# ===========================
# REST FRAMEWORK
# ===========================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
