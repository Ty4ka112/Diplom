from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Priority

class PriorityAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.priority = Priority.objects.create(name='High')

    def test_create_priority(self):
        url = reverse('priority-list')
        data = {
            'name': 'Low'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_priority(self):
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'High')

    def test_update_priority(self):
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        data = {'name': 'Updated Priority'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Priority')

    def test_delete_priority(self):
        url = reverse('priority-detail', kwargs={'pk': self.priority.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
