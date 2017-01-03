# -*- encoding: utf-8 -*-
import os
import json


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# CONFIGURACION GENERAL DEL PROYECTO
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Arbol de directorios
--------------------
* PROJECT_DIR
    Directorio de este archivo 'settings.py'

* BASE_DIR
    Directorio base del proyecto, el directorio contenedor de 'PROJECT_DIR'

* MEDIA_ROOT
    Directorio donde guardar los objetos subidos por el usuario

* STATIC_ROOT
    Directorio donde se almacenan los archivos estaticos del proyecto al
    ejecutar el comando 'python manage.py collectstatic'

* STATICFILES_DIRS
    Directorios de archivos staticos adicionales
    El unico directorio que hemos incluido aqui es un directorio
    'static' que esta dentro del 'Project Dir'

* STATICFILES_DIRS
    Directorios de archivos staticos adicionales
    El unico directorio que hemos incluido aqui es un directorio
    'static' que esta dentro del 'Project Dir'
"""
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'public', 'media'))
STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'public', 'static'))

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


"""
Administradores
---------------
Adminsitradores de sistemas: supervisores de la empresa desarrolaldora
(SoftButterfly) y sypervisores de la empresa cliente (DGT Alliance).
Si 'DEBUG' (ver mas adelante) es False entonces Django envia el detale completo
de los errores cada vez que se producen.
"""
ADMINS = (
    ('SoftButterfly System Administrator', 'sysadmin@softbutterfly.space'),
    ('HackSpace System Administrator', 'sysadmin@hackspace.pe'),
)

MANAGERS = ADMINS


"""
Seguridad
---------
* SECRET_KEY
    Llave se seguridad empleada para firmar elementos que se guardan con
    encriptación.
* ALLOWED_HOSTS
    Una lista de los nombres de los sitios web que estre proyecto django
    servirá, pueden ser un nombre completo ('www.example.com') o contener
    comodines ('*.example.com'). Durante el desarrollo empleamos el valor '*'
    para aceptar cualquier dominio
"""
SECRET_KEY = os.getenv('SECRET_KEY', '$Up#r*$#CR#T*k#i')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(':')
INTERNAL_IPS = os.getenv('INTERNAL_IPS', '127.0.0.1').split()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


"""
Debug
-----
* DEBUG
    El sitio esta en modo debug solo en fase de desarrollo
"""
DEBUG = json.loads(os.getenv('DEBUG_SITE', 'true'))


"""
Apicaciones instaladas
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicaciones Locales
    'sample_app'
]


"""
Middlewares
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


"""
URLS
----
* ROOT_URLCONF
    Es la lista de las utls que maneja la aplicacion de django
* STATIC_URL y MEDIA_URL
    Son las urls con las que se hara referencia a los archivos almacenados en
    las ubicaciones STATIC_ROOT y MEDIA_ROOT respectivamente. Estas URLs pueden
    ser manejadas por django o, preferiblemente, por un programa servidor
    externo como nginx o httpd
"""
ROOT_URLCONF = 'sample_project.urls'
STATIC_URL = os.getenv('STATIC_URL', '/static/')
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')


"""
Plantillas de HTML
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': json.loads(os.getenv('DEBUG_TEMPLATES', 'true')),
        },
    },
]


"""
Aplicacion de WSGI
------------------
    Es el modulo que permitira manejar la aplicacion de django como una
    aplicacion wsgi para cominicarse con un programa servidor externo como
    nginx o httpd
"""
WSGI_APPLICATION = 'sample_project.wsgi.application'


"""
Bases de Datos
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


"""
Autenticación
"""
AUTH_USER_MODEL = 'auth.User'

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


"""
Internacionalization and localization
"""
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = os.getenv('TIME_ZONE', 'America/Lima')
USE_I18N = True
USE_L10N = True
USE_TZ = True

