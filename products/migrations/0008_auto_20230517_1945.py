# Generated by Django 2.1 on 2023-05-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prod_description',
            field=models.CharField(default='they are nice', max_length=10000),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_stock',
            field=models.IntegerField(blank=True, default=100),
        ),
    ]