from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='In Progress',
            priority='Medium',
            due_date='2024-07-01T12:00:00Z',
            category='Test Category',
            assigned_to=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.status, 'In Progress')
