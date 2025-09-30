from django.test import TestCase
from django.contrib.auth import get_user_model

user = get_user_model()

class TaskAPITest(TestCase):
    def setUp(self):
        self.user = user.objects.create_user(
            email="test@example.com",
            full_name="Test User",
            phone_no="1234567890",
            password="password123"
        )

        response = self.client.post("/api/v1/login/", {
            "username": "test@example.com",
            "password": "password123"
        }, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.token = response.json().get("token") 

        self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}

    def test_task_create(self):
        response = self.client.post(
            "/api/v1/tasks/",
            data={"title": "Test Task", "description": "Testing ninja"},
            content_type="application/json",
            **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_task_list(self):
        self.client.post(
            "/api/v1/tasks/",
            data={"title": "Task 1", "description": "First"},
            content_type="application/json",
            **self.auth_headers
        )

        response = self.client.get("/api/v1/tasks/?offset=0&limit=5", **self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_task_update(self):
        create_res = self.client.post(
            "/api/v1/tasks/",
            data={"title": "Old Title", "description": "Old desc"},
            content_type="application/json",
            **self.auth_headers
        )
        task_id = create_res.json()["data"]["id"]

        response = self.client.put(
            f"/api/v1/tasks/{task_id}/",
            data={"title": "New Title", "description": "Updated desc", "completed": False},
            content_type="application/json",
            **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["title"], "New Title")

    def test_task_delete(self):
        create_res = self.client.post(
            "/api/v1/tasks/",
            data={"title": "To Delete", "description": "Temp"},
            content_type="application/json",
            **self.auth_headers
        )
        task_id = create_res.json()["data"]["id"]

        response = self.client.delete(f"/api/v1/tasks/{task_id}/", **self.auth_headers)
        self.assertEqual(response.status_code, 200)

    def test_mark_completed(self):
        create_res = self.client.post(
            "/api/v1/tasks/",
            data={"title": "Incomplete", "description": "Test mark"},
            content_type="application/json",
            **self.auth_headers
        )
        task_id = create_res.json()["data"]["id"]

        response = self.client.patch(
            f"/api/v1/mark/tasks/{task_id}/",
            data={"completed": True},
            content_type="application/json",
            **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["data"]["completed"])

