# Generated by Django 4.2.8 on 2024-02-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_itembucket_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itembucket',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product'),
        ),
    ]
