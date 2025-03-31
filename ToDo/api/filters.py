from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):

    class Meta:
        # Модель, которую будем фильтровать
        model = Task
        # Фильтры
        fields = {
            'status': ['exact'],
            'category': ['exact'],
            'priority': ['exact'],
            'created_at': ['gte', 'lte'],
        }
