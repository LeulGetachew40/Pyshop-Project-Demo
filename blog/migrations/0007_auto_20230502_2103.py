# Generated by Django 2.1 on 2023-05-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='comment',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='likes_counter',
            field=models.IntegerField(blank=True),
        ),
    ]
