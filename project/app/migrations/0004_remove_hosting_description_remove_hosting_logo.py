# Generated by Django 5.0 on 2024-05-16 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_subject_contact_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosting',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hosting',
            name='logo',
        ),
    ]
