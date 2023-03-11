# Generated by Django 4.1.7 on 2023-03-11 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cart", "0001_initial"),
        ("lectures", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="lecture",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to="lectures.lecture",
            ),
        ),
    ]