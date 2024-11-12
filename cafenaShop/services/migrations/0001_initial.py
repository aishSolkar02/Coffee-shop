# Generated by Django 5.1.2 on 2024-10-25 12:42

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100)),
                ('menu_price', models.PositiveIntegerField(default=50)),
                ('menu_image', models.ImageField(upload_to='services/')),
            ],
            managers=[
                ('customManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
