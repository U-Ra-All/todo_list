from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse

from app.forms import TaskCreationForm
from app.models import Task, Tag
from app.tests.utils import setup_test_task_with_tags


class TaskCreationFormTest(TestCase):
    def test_task_create_form_deadline_datetime_label(self):
        form = TaskCreationForm()
        self.assertTrue(
            (form.fields["deadline_datetime"].label is None
             or form.fields["deadline_datetime"].label == "Deadline date and time (optional)")
        )

    def test_task_create_form_deadline_datetime_placeholder(self):
        form = TaskCreationForm()
        self.assertTrue(
            form
            .fields["deadline_datetime"]
            .widget
            .attrs["placeholder"] == "e.g. 2006-10-25 14:30"
        )


class UpdateFormsHaveInitialValuesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        setup_test_task_with_tags()

    def test_task_update_form_has_initial_value(self):
        response = self.client.get(reverse(
            "app:task-update",
            kwargs={"pk": 6}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["content"],
            "TestTask"
        )
        self.assertEqual(
            response.context["form"].initial["deadline_datetime"],
            datetime(2026, 10, 25, 12, 30, tzinfo=timezone.utc)
        )
        self.assertEqual(
            response.context["form"].initial["done"],
            False
        )
        self.assertEqual(
            response.context["form"].initial["tags"],
            list(Tag.objects.all())
        )

    def test_tag_update_form_has_initial_value(self):
        response = self.client.get(reverse(
            "app:tag-update",
            kwargs={"pk": 5}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["name"],
            "TestTag1"
        )
