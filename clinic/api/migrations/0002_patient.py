# Generated by Django 4.2.5 on 2024-02-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=50)),
                ("contact", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
    ]
