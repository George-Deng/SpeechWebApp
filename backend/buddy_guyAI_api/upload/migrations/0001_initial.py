# Generated by Django 3.2.2 on 2021-07-13 22:31

import buddy_guyAI_api.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=buddy_guyAI_api.storage_backends.PublicMediaStorage(), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UploadPrivate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=buddy_guyAI_api.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
    ]