# Generated by Django 3.2.19 on 2023-12-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_products_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
