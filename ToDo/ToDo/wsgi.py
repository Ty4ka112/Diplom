"""
WSGI config for ToDo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Импортируем модуль os для работы с операционной системой
import os

# Импортируем функцию get_wsgi_application из django.core.wsgi для получения WSGI приложения
from django.core.wsgi import get_wsgi_application

# Устанавливаем значение переменной окружения DJANGO_SETTINGS_MODULE на ToDo.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo.settings')

# Получаем WSGI приложение и назначаем его переменной application
application = get_wsgi_application()
