from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
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

    def get_absolute_url(self):
        return reverse("app:task-list")
