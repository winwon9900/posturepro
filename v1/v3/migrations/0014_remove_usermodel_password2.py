# Generated by Django 5.0.4 on 2024-04-13 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0013_remove_usermodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='password2',
        ),
    ]
