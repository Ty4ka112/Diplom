from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category

class CategoryAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Work', description='Work related tasks')

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            'name': 'Home',
            'description': 'Home related tasks'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Work')

    def test_update_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        data = {'name': 'Updated Category'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Category')

    def test_delete_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
