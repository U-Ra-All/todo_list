# Generated by Django 4.2 on 2023-04-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline_datetime", models.DateTimeField(null=True)),
                ("done", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(related_name="tasks", to="app.tag")),
            ],
        ),
    ]
