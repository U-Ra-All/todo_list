# Generated by Django 4.2 on 2023-05-02 12:12

from django.db import migrations
from django.db.migrations import RunPython


def func(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "fixture_data.json")


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_task_options"),
    ]

    operations = [
        RunPython(func, reverse_func)
    ]
