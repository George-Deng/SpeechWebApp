# Generated by Django 3.2.2 on 2021-07-20 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210718_1253'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLoginActivity',
        ),
    ]