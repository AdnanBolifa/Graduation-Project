# Generated by Django 5.0.4 on 2024-05-24 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_disease', '0004_remove_doctorfeedback_feedback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienthistory',
            name='doctorFeedback',
        ),
    ]