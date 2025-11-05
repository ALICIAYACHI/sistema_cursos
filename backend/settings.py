"""
Django settings for backend project.
Configurado para funcionar localmente (MySQL) y en Render (PostgreSQL).
"""

from pathlib import Path
import os
import dj_database_url

# ===========================
# BASE DIR
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# CONFIGURACIÓN GENERAL
# ===========================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temporal')

# Render define la variable 'RENDER' en entorno de producción
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# ✅ Confianza para CSRF desde Render
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://sistema-cursos-frontend.onrender.com',
]

# ===========================
# APLICACIONES INSTALADAS
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de terceros
    'rest_framework',
    'corsheaders',

    # App local
    'cursos',
]

# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ debe ir arriba
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ⚡ para servir estáticos en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# CORS CONFIG
# ===========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",                      # desarrollo local
    "http://127.0.0.1:3000",                      # desarrollo local alternativo
    "https://sistema-cursos-frontend.onrender.com"  # ✅ frontend en Render
]

CORS_ALLOW_CREDENTIALS = True

# Si necesitas permitir temporalmente todos los orígenes (solo para debug)
# CORS_ALLOW_ALL_ORIGINS = True

# ===========================
# URLS Y WSGI
# ===========================
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # opcional
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
if os.environ.get('RENDER'):  # ✅ entorno Render (usa PostgreSQL)
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
else:  # ✅ entorno local (usa MySQL)
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

# ===========================
# REST FRAMEWORK
# ===========================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# ===========================
# CLAVE PRIMARIA POR DEFECTO
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
