# Generated by Django 4.1.7 on 2023-03-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
