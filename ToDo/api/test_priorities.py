from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Priority

# Определяем класс PriorityAPITests, который наследует от APITestCase для создания тестов API
class PriorityAPITests(APITestCase):
    # Метод setUp используется для предварительной настройки тестовых данных
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Аутентифицируем клиента с помощью созданного пользователя
        self.client.force_authenticate(user=self.user)
        # Создаем приоритет для тестирования
        self.priority = Priority.objects.create(name='High')

    # Тестовый метод для создания нового приоритета
    def test_create_priority(self):
        # Строим URL-адрес для создания приоритета
        url = reverse('priority-list')
        # Определяем данные для нового приоритета
        data = {
            'name': 'Low'
        }
        # Отправляем POST-запрос для создания приоритета
        response = self.client.post(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тестовый метод для получения приоритета
    def test_get_priority(self):
        # Строим URL-адрес для получения приоритета по первичному ключу
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        # Отправляем GET-запрос для получения приоритета
        response = self.client.get(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что имя приоритета совпадает с ожидаемым значением
        self.assertEqual(response.data['name'], 'High')

    # Тестовый метод для обновления приоритета
    def test_update_priority(self):
        # Строим URL-адрес для обновления приоритета по первичному ключу
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        # Определяем данные для обновления приоритета
        data = {'name': 'Updated Priority'}
        # Отправляем PATCH-запрос для обновления приоритета
        response = self.client.patch(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что имя приоритета обновлено на ожидаемое значение
        self.assertEqual(response.data['name'], 'Updated Priority')

    # Тестовый метод для удаления приоритета
    def test_delete_priority(self):
        # Строим URL-адрес для удаления приоритета по первичному ключу
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        # Отправляем DELETE-запрос для удаления приоритета
        response = self.client.delete(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
