from django.db import models
from django.contrib.auth.models import User

# Определяем приоритет задач
class Priority(models.Model):
    objects = None
    # для приоритетов
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    # для возвращения представления приоритета
    def __str__(self):
        return self.name

# Определяем модель Category для категорий задач
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    # для описания категории
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    # для возвращения строкового представления категории
    def __str__(self):
        return self.name

# модель Task для задач
class Task(models.Model):
    # для выбора статуса задачи
    objects = None
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)

    # для возвращения строкового представления заголовка задачи
    def __str__(self):
        return self.title
