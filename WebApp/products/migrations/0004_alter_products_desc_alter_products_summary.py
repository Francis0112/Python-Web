# Generated by Django 4.1.5 on 2023-02-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(default='summary...'),
        ),
    ]
