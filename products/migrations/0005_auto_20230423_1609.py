# Generated by Django 2.1 on 2023-04-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
