# Generated by Django 4.1.3 on 2023-03-08 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lectures", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("videoFile", models.URLField()),
                ("videoLength", models.IntegerField(default=0)),
                (
                    "lecture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lectures.lecture",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
