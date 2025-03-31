"""
ASGI config for ToDo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Импортируем модуль os для работы с операционной системой
import os

# Импортируем функцию get_asgi_application из django.core.asgi для получения ASGI приложения
from django.core.asgi import get_asgi_application

# Устанавливаем значение переменной окружения DJANGO_SETTINGS_MODULE на ToDo.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo.settings')

# Получаем ASGI приложение и назначаем его переменной application
application = get_asgi_application()
