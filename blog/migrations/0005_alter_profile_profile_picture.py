# Generated by Django 4.0.4 on 2022-08-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_picture.jpg', null=True, upload_to=''),
        ),
    ]