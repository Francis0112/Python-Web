# Generated by Django 4.1.5 on 2023-02-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cars_alter_products_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(default='onegai shi masu'),
        ),
    ]