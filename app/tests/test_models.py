from django.test import TestCase

from app.models import Task, Tag


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_task = Task.objects.create(
            content="TestTask",
            deadline_datetime="2026-10-25 14:30")

        Tag.objects.create(
            name="TestTag1"
        )

        Tag.objects.create(
            name="TestTag2"
        )

        tags_for_task = Tag.objects.all()
        test_task.tags.set(tags_for_task)
        test_task.save()

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_datetime_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("datetime").verbose_name
        self.assertEqual(field_label, "datetime")

    def test_deadline_datetime_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("deadline_datetime").verbose_name
        self.assertEqual(field_label, "deadline datetime")

    def test_done_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("done").verbose_name
        self.assertEqual(field_label, "done")

    def test_tags_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("tags").verbose_name
        self.assertEqual(field_label, "tags")

    def test_task_str(self):
        task = Task.objects.get(id=1)
        expected_object_name = f"{task.content}. " \
                               f"Tags: ({', '.join([tag.name for tag in task.tags.all()])})"
        self.assertEqual(str(task), expected_object_name)

    def test_get_absolute_url(self):
        task = Task.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(task.get_absolute_url(), "/")
