from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, Category, Priority

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Work')
        self.priority = Priority.objects.create(name='High')
        self.task1 = Task.objects.create(
            created_by=self.user,
            title='Test Task 1',
            description='Test Description 1',
            status='pending',
            category=self.category,
            priority=self.priority
        )
        self.task2 = Task.objects.create(
            created_by=self.user,
            title='Test Task 2',
            description='Test Description 2',
            status='completed',
            category=self.category,
            priority=self.priority
        )

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'status': 'pending',
            'category': self.category.pk,
            'priority': self.priority.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task 1')

    def test_update_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        data = {'title': 'Updated Task'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_tasks_by_status(self):
        url = reverse('task-list') + '?status=pending'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task 1')

    def test_order_tasks_by_created_at(self):
        url = reverse('task-list') + '?ordering=created_at'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Task 1')
        self.assertEqual(response.data[1]['title'], 'Test Task 2')
