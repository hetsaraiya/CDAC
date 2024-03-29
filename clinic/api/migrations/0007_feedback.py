# Generated by Django 3.2.8 on 2024-02-26 10:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_appointment_patient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('gender', models.CharField(default='', max_length=20)),
                ('rate', models.CharField(default='', max_length=20)),
                ('comment', models.TextField()),
                ('recieve', models.BooleanField(default=False)),
                ('contact', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
            ],
        ),
    ]
