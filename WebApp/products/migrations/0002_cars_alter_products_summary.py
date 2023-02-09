# Generated by Django 4.1.5 on 2023-02-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=120)),
                ('drive', models.CharField(max_length=120)),
                ('fuel', models.CharField(max_length=120)),
                ('mileage', models.CharField(max_length=120)),
                ('owner', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(default='item summary...'),
        ),
    ]