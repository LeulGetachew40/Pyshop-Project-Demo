# Generated by Django 2.1 on 2023-04-23 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230423_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='featured',
        ),
    ]
