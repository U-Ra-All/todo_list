from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )
