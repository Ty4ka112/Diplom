from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, Category, Priority

# Определяем класс TaskAPITests, который наследует от APITestCase для создания тестов API
class TaskAPITests(APITestCase):
    # Метод setUp используется для предварительной настройки тестовых данных
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Аутентифицируем клиента с помощью созданного пользователя
        self.client.force_authenticate(user=self.user)
        # Создаем категорию для тестирования
        self.category = Category.objects.create(name='Work')
        # Создаем приоритет для тестирования
        self.priority = Priority.objects.create(name='High')
        # Создаем первую задачу для тестирования
        self.task1 = Task.objects.create(
            created_by=self.user,
            title='Test Task 1',
            description='Test Description 1',
            status='pending',
            category=self.category,
            priority=self.priority
        )
        # Создаем вторую задачу для тестирования
        self.task2 = Task.objects.create(
            created_by=self.user,
            title='Test Task 2',
            description='Test Description 2',
            status='completed',
            category=self.category,
            priority=self.priority
        )

    # Тестовый метод для создания новой задачи
    def test_create_task(self):
        # Строим URL-адрес для создания задачи
        url = reverse('task-list')
        # Определяем данные для новой задачи
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'status': 'pending',
            'category': self.category.pk,
            'priority': self.priority.pk
        }
        # Отправляем POST-запрос для создания задачи
        response = self.client.post(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тестовый метод для получения задачи
    def test_get_task(self):
        # Строим URL-адрес для получения задачи по первичному ключу
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        # Отправляем GET-запрос для получения задачи
        response = self.client.get(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что заголовок задачи совпадает с ожидаемым значением
        self.assertEqual(response.data['title'], 'Test Task 1')

    # Тестовый метод для обновления задачи
    def test_update_task(self):
        # Строим URL-адрес для обновления задачи по первичному ключу
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        # Определяем данные для обновления задачи
        data = {'title': 'Updated Task'}
        # Отправляем PATCH-запрос для обновления задачи
        response = self.client.patch(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что заголовок задачи обновлен на ожидаемое значение
        self.assertEqual(response.data['title'], 'Updated Task')

    # Тестовый метод для удаления задачи
    def test_delete_task(self):
        # Строим URL-адрес для удаления задачи по первичному ключу
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        # Отправляем DELETE-запрос для удаления задачи
        response = self.client.delete(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Тестовый метод для фильтрации задач по статусу
    def test_filter_tasks_by_status(self):
        # Строим URL-адрес для фильтрации задач по статусу
        url = reverse('task-list') + '?status=pending'
        # Отправляем GET-запрос для фильтрации задач
        response = self.client.get(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что в ответе только одна задача
        self.assertEqual(len(response.data), 1)
        # Проверяем, что заголовок задачи совпадает с ожидаемым значением
        self.assertEqual(response.data[0]['title'], 'Test Task 1')

    # Тестовый метод для сортировки задач по дате создания
    def test_order_tasks_by_created_at(self):
        # Строим URL-адрес для сортировки задач по дате создания
        url = reverse('task-list') + '?ordering=created_at'
        # Отправляем GET-запрос для сортировки задач
        response = self.client.get(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что задачи отсортированы в ожидаемом порядке
        self.assertEqual(response.data[0]['title'], 'Test Task 1')
        self.assertEqual(response.data[1]['title'], 'Test Task 2')
