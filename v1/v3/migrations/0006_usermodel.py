# Generated by Django 5.0.4 on 2024-04-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v3', '0005_document_delete_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=20)),
                ('rank', models.IntegerField(default='', max_length=100)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'my-user',
            },
        ),
    ]
