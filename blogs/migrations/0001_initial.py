# Generated by Django 4.2.13 on 2024-05-26 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("created_on", models.DateTimeField()),
                ("content", models.TextField()),
                (
                    "meta_description",
                    models.CharField(default="new post", max_length=300),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Publish"), (2, "Delete")], default=0
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]