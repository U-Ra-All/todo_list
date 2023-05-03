from app.models import Task, Tag


def setup_test_task_with_tags():
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
