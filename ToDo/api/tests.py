from django.test import TestCase
from django.contrib.auth.models import User

# Определяем класс UserTests, который наследует от TestCase для создания тестов
class UserTests(TestCase):
    # Метод setUp используется для предварительной настройки тестовых данных
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # Тестовый метод для создания нового пользователя
    def test_create_user(self):
        # Создаем нового пользователя
        user = User.objects.create_user(username='newuser', password='newpassword')
        # Проверяем, что количество пользователей в базе данных равно 2
        self.assertEqual(User.objects.count(), 2)

    # Тестовый метод для получения пользователя
    def test_get_user(self):
        # Получаем пользователя с именем пользователя 'testuser'
        user = User.objects.get(username='testuser')
        # Проверяем, что имя пользователя совпадает с ожидаемым значением
        self.assertEqual(user.username, 'testuser')

    # Тестовый метод для обновления пользователя
    def test_update_user(self):
        # Получаем пользователя с именем пользователя 'testuser'
        user = User.objects.get(username='testuser')
        # Обновляем имя пользователя
        user.username = 'updateduser'
        # Сохраняем изменения
        user.save()
        # Проверяем, что имя пользователя обновлено на ожидаемое значение
        self.assertEqual(user.username, 'updateduser')

    # Тестовый метод для удаления пользователя
    def test_delete_user(self):
        # Получаем пользователя с именем пользователя 'testuser'
        user = User.objects.get(username='testuser')
        # Удаляем пользователя
        user.delete()
        # Проверяем, что количество пользователей в базе данных равно 0
        self.assertEqual(User.objects.count(), 0)
