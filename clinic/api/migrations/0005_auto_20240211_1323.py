# Generated by Django 3.2.8 on 2024-02-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_doctor_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor_details',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]