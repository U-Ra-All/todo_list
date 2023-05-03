from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("app:tag-list")


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-datetime"]

    def __str__(self):
        return f"{self.content}. " \
               f"Tags: ({', '.join([tag.name for tag in self.tags.all()])})"

    @staticmethod
    def get_absolute_url():
        return reverse("app:task-list")
