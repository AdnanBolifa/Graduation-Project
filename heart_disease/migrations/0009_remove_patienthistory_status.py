# Generated by Django 5.0.4 on 2024-05-25 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_disease', '0008_patienthistory_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienthistory',
            name='status',
        ),
    ]
