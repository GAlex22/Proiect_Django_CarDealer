# Generated by Django 4.0.6 on 2022-08-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_image_main_car_image_rename_brand_car_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='name',
            new_name='Name',
        ),
    ]
