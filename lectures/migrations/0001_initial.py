# Generated by Django 4.1.7 on 2023-03-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lecture",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("LectureId", models.AutoField(primary_key=True, serialize=False)),
                ("lectureTitle", models.CharField(max_length=100)),
                (
                    "lectureDifficulty",
                    models.CharField(
                        choices=[
                            ("easy", "Easy"),
                            ("middle", "Middle"),
                            ("hard", "Hard"),
                        ],
                        max_length=20,
                    ),
                ),
                ("lectureDescription", models.TextField(max_length=1000)),
                ("targetAudience", models.CharField(max_length=30)),
                ("lectureFee", models.PositiveIntegerField()),
                ("thumbnail", models.URLField()),
                ("lecturePeriod", models.DurationField()),
                ("isOpened", models.BooleanField(default=True)),
                ("lectureDuration", models.PositiveIntegerField(default=0)),
                ("lectureTotal", models.PositiveIntegerField(default=0)),
                ("likes", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]