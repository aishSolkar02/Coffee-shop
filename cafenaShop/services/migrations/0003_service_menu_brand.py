# Generated by Django 5.1.2 on 2024-11-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='menu_brand',
            field=models.CharField(default='coffee', max_length=100),
        ),
    ]
