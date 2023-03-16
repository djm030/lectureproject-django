# Generated by Django 4.1.7 on 2023-03-16 04:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ledetailes", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("loginDate", models.DateTimeField(auto_now=True)),
                ("lectureDate", models.DateTimeField(auto_now=True)),
                ("paymentDate", models.DateTimeField(auto_now=True)),
                ("isWithdrawn", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("Withdrawn_at", models.DateTimeField(auto_now=True)),
                ("password", models.CharField(max_length=100)),
                ("memberId", models.AutoField(primary_key=True, serialize=False)),
                ("nickname", models.CharField(blank=True, max_length=30, null=True)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(blank=True, max_length=30, null=True)),
                ("dateBirth", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("phoneNumber", models.CharField(max_length=20)),
                ("profileImg", models.URLField(blank=True, max_length=50, null=True)),
                (
                    "isInstructor",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("first_name", models.CharField(editable=False, max_length=20)),
                ("last_name", models.CharField(editable=False, max_length=20)),
                (
                    "instructorField",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "instructorAbout",
                    models.TextField(blank=True, default="", max_length=500),
                ),
                (
                    "instructorCareer",
                    models.TextField(blank=True, default="", max_length=50),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "ledetaile",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="user",
                        to="ledetailes.ledetaile",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
