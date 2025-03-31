from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category

# Определяем класс CategoryAPITests, который наследует от APITestCase для создания тестов API
class CategoryAPITests(APITestCase):
    # Метод setUp используется для предварительной настройки тестовых данных
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Аутентифицируем клиента с помощью созданного пользователя
        self.client.force_authenticate(user=self.user)
        # Создаем категорию для тестирования
        self.category = Category.objects.create(name='Work', description='Work related tasks')

    # Тестовый метод для создания новой категории
    def test_create_category(self):
        # Строим URL-адрес для создания категории
        url = reverse('category-list')
        # Определяем данные для новой категории
        data = {
            'name': 'Home',
            'description': 'Home related tasks'
        }
        # Отправляем POST-запрос для создания категории
        response = self.client.post(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тестовый метод для получения категории
    def test_get_category(self):
        # Строим URL-адрес для получения категории по первичному ключу
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        # Отправляем GET-запрос для получения категории
        response = self.client.get(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что имя категории совпадает с ожидаемым значением
        self.assertEqual(response.data['name'], 'Work')

    # Тестовый метод для обновления категории
    def test_update_category(self):
        # Строим URL-адрес для обновления категории по первичному ключу
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        # Определяем данные для обновления категории
        data = {'name': 'Updated Category'}
        # Отправляем PATCH-запрос для обновления категории
        response = self.client.patch(url, data, format='json')
        # Проверяем, что ответ имеет статус HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что имя категории обновлено на ожидаемое значение
        self.assertEqual(response.data['name'], 'Updated Category')

    # Тестовый метод для удаления категории
    def test_delete_category(self):
        # Строим URL-адрес для удаления категории по первичному ключу
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        # Отправляем DELETE-запрос для удаления категории
        response = self.client.delete(url, format='json')
        # Проверяем, что ответ имеет статус HTTP 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
