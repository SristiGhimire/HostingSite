# Generated by Django 5.0 on 2024-05-13 05:26

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='aboutimage')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='clientlogo')),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyAddress', models.CharField(max_length=200)),
                ('companyPhone', models.CharField(max_length=200)),
                ('companyEmail', models.EmailField(max_length=254)),
                ('addressUrl', models.URLField(max_length=2000)),
                ('companyLogo', models.FileField(upload_to='companylogo')),
                ('facebookUrl', models.URLField()),
                ('linkedInUrl', models.URLField()),
                ('twiterUrl', models.URLField()),
                ('discordUrl', models.URLField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='HeroBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='herobannerimage')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='Hostingimage/')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='HostingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='HostingServiceimage/')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='Serviceimage/')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HostingPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectPackages', models.CharField(choices=[('personal', 'Personal'), ('business', 'Business'), ('enterprise', 'Enterprise')], max_length=150)),
                ('storage', models.FloatField()),
                ('bandwidth', models.CharField(max_length=200)),
                ('support', models.BooleanField(default=True)),
                ('domain', models.BooleanField(default=True)),
                ('accountResold', models.PositiveIntegerField()),
                ('feePerMonth', models.FloatField()),
                ('hosting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hostings', to='app.hosting')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]