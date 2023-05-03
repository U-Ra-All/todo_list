from django.test import TestCase
from django.urls import reverse

from app.models import Task, Tag

TASKS_URL = reverse("app:task-list")
TAGS_URL = reverse("app:tag-list")


class TaskListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 tasks for pagination tests + 5 from fixture
        number_of_tasks = 10

        for task_id in range(number_of_tasks):
            test_task = Task.objects.create(
                content=f"TestTask {task_id}",
                deadline_datetime=f"2026-10-25 14:30")

            Tag.objects.create(
                name=f"TestTag1 {task_id}"
            )

            Tag.objects.create(
                name=f"TestTag2 {task_id}"
            )

            tags_for_task = Tag.objects.all()
            test_task.tags.set(tags_for_task)
            test_task.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(TASKS_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(TASKS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/task_list.html")

    def test_pagination_is_5(self):
        response = self.client.get(TASKS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["task_list"]), 5)

    def test_lists_all_tasks(self):
        # Get the third page and confirm it has (exactly) remaining 3 items
        response = self.client.get(TASKS_URL + "?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["task_list"]), 5)


class TagListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 tags for pagination tests + 4 from fixture
        number_of_tags = 10

        for tag_id in range(number_of_tags):
            Tag.objects.create(name=f"TestTag {tag_id}")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(TAGS_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(TAGS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/tag_list.html")

    def test_pagination_is_5(self):
        response = self.client.get(TAGS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["tag_list"]), 5)

    def test_lists_all_tags(self):
        # Get the third page and confirm it has (exactly) remaining 3 items
        response = self.client.get(TAGS_URL + "?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["tag_list"]), 4)
