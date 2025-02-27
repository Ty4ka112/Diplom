from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task, Category, Priority

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_user(self):
        user = User.objects.create_user(username='newuser', password='newpassword')
        self.assertEqual(User.objects.count(), 2)

    def test_get_user(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')

    def test_update_user(self):
        user = User.objects.get(username='testuser')
        user.username = 'updateduser'
        user.save()
        self.assertEqual(user.username, 'updateduser')

    def test_delete_user(self):
        user = User.objects.get(username='testuser')
        user.delete()
        self.assertEqual(User.objects.count(), 0)
