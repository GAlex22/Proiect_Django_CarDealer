# Generated by Django 4.0.6 on 2022-08-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_name_car_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Name',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='image',
            new_name='image_main',
        ),
        migrations.AddField(
            model_name='car',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car',
            name='image4',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='car',
            name='image5',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
