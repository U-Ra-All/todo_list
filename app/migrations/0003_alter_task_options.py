# Generated by Django 4.2 on 2023-05-01 05:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_task_deadline_datetime"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["done", "-datetime"]},
        ),
    ]
