from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskModelTest(TestCase):
  def setUp(self):
    Task.objects.create(title="Test Task", description="Test Description")

  def test_task_creation(self):
    task = Task.objects.get(title="Test Task")
    self.assertEqual(task.description, "Test Description")
    self.assertFalse(task.completed)

class TaskViewSetTest(APITestCase):
  def test_view_tasks(self):
    url = reverse('task-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)