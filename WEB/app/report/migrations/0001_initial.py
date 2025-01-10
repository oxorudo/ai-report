# Generated by Django 4.2.16 on 2025-01-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LessonData",
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
                ("mcode", models.CharField(max_length=255)),
                ("l_title", models.CharField(max_length=255)),
                ("unique_content_nm", models.CharField(max_length=255)),
                ("leccode", models.CharField(max_length=255)),
                ("u_title", models.CharField(max_length=255)),
                ("content_grade", models.IntegerField()),
                ("term", models.IntegerField()),
            ],
        ),
    ]