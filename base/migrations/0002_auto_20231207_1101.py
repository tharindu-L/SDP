# Generated by Django 3.2.19 on 2023-12-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='products',
            field=models.ManyToManyField(to='base.Category'),
        ),
    ]
