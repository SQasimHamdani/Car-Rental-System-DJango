# Generated by Django 3.0.6 on 2021-05-05 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_remove_saleorder_salesman'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorder',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
