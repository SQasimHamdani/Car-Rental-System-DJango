# Generated by Django 3.0.6 on 2021-05-02 18:49

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(default='car-images/car-default.png', storage=system.models.OverwriteStorage(), upload_to=system.models.rename_car_profile_uploaded_file),
        ),
    ]
