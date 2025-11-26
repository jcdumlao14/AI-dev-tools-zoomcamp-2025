from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.client.post(reverse("add"), {
            "title": "Test Todo",
            "description": "Testing add"
        })
        self.assertEqual(Todo.objects.count(), 1)

    def test_toggle_complete(self):
        todo = Todo.objects.create(title="Test", description="Test Desc")
        self.client.get(reverse("complete", args=[todo.id]))
        todo.refresh_from_db()
        self.assertTrue(todo.completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title="To delete")
        self.client.get(reverse("delete", args=[todo.id]))
        self.assertEqual(Todo.objects.count(), 0)
