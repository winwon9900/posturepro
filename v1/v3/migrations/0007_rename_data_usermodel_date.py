# Generated by Django 5.0.4 on 2024-04-13 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0006_usermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='data',
            new_name='date',
        ),
    ]
