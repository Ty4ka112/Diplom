# Импортируем класс AppConfig из модуля django.apps
from django.apps import AppConfig

# Определяем класс ApiConfig, который наследует от AppConfig
class ApiConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'api'

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from .models import Category, Priority

        categories = ['Работа', 'Учёба', 'Домашние дела', 'Путешествия']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        priorities = ['Низкий', 'Средний', 'Высокий', 'Критический']
        for priority_name in priorities:
            Priority.objects.get_or_create(name=priority_name)
