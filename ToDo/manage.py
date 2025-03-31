#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE на ToDo.settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo.settings')
    try:
        # Импортируем функцию execute_from_command_line из django.core.management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Генерируем исключение, если Django не установлен или отсутствует в PYTHONPATH
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Выполняем команду из командной строки
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
