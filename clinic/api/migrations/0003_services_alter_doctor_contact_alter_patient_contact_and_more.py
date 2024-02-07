# Generated by Django 4.2.5 on 2024-02-07 16:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_patient"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("speciality_title", models.CharField(max_length=20)),
                ("speciality_description", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="doctor",
            name="contact",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="contact",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
        migrations.CreateModel(
            name="Appointment",
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
                (
                    "patient_contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("patient_email", models.EmailField(max_length=254)),
                ("appointment_date", models.DateField()),
                ("appointment_time", models.TimeField()),
                ("description", models.TextField()),
                (
                    "doctor_details",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.doctor",
                    ),
                ),
                (
                    "patient_details",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.patient",
                    ),
                ),
            ],
        ),
    ]
