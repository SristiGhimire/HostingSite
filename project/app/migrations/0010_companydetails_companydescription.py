# Generated by Django 5.0 on 2024-05-19 11:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='companyDescription',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
