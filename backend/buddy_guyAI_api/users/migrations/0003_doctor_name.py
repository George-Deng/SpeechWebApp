# Generated by Django 3.2.2 on 2021-07-16 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
