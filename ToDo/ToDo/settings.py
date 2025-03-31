import os
from pathlib import Path
from datetime import timedelta

# Устанавливаем базовую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Устанавливаем секретный ключ для проекта
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-$7hs5+2qxlkd4m)lyn%%n1l_7y$hr97l^z8=vwquya$+v0kbwo')

# Устанавливаем режим отладки
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Список допустимых хостов
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',  # Приложение администрирования Django
    'django.contrib.auth',  # Приложение аутентификации и авторизации Django
    'django.contrib.contenttypes',  # Приложение типов контента Django
    'django.contrib.sessions',  # Приложение сессий Django
    'django.contrib.messages',  # Приложение сообщений Django
    'django.contrib.staticfiles',  # Приложение для работы со статическими файлами Django
    'rest_framework',  # Приложение Django REST Framework
    'rest_framework_simplejwt',  # Приложение для работы с JWT аутентификацией
    'rest_framework.authtoken',  # Приложение для токенов аутентификации
    'api',  # Приложение API
    'django_filters',  # Приложение для фильтрации запросов
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Класс аутентификации JWT
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Класс разрешений, требующий аутентификации
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',  # Класс фильтрации запросов
    ],
}

# Настройки SIMPLE_JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Время жизни токена доступа
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Время жизни токена обновления
    'ROTATE_REFRESH_TOKENS': False,  # Не вращать токены обновления
    'BLACKLIST_AFTER_ROTATION': True,  # Добавлять токены в чёрный список после ротации
    'ALGORITHM': 'HS256',  # Алгоритм шифрования
    'SIGNING_KEY': SECRET_KEY,  # Ключ подписи
    'AUTH_HEADER_TYPES': ('Bearer',),  # Тип заголовка аутентификации
    'USER_ID_FIELD': 'id',  # Поле идентификатора пользователя
    'USER_ID_CLAIM': 'user_id',  # Поле требования идентификатора пользователя
}

# Определяем список MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  #  безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',  #  для обработки сессий
    'django.middleware.common.CommonMiddleware',  # Общее
    'django.middleware.csrf.CsrfViewMiddleware',  #  защита от CSRF атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #  аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  #  сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # защиты от Clickjacking атак
]

# Устанавливаем корневую конфигурацию URL
ROOT_URLCONF = 'ToDo.urls'

# Определяем настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Устанавливаем WSGI_APPLICATION
WSGI_APPLICATION = 'ToDo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Бэкэнд базы данных SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу базы данных
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Валидатор на схожесть атрибутов
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Валидатор на минимальную длину пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Валидатор на общие пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Валидатор на числовые пароли
    },
]

LOGIN_REDIRECT_URL = '/tasks/'  # Перенаправление на главную страницу после входа

LANGUAGE_CODE = 'ru'  #
TIME_ZONE = 'UTC'  #
USE_I18N = True  #
USE_TZ = True  #

# Настройки статических файлов
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Поле авто инкремента по умолчанию для моделей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
