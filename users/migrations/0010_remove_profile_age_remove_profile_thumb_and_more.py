# Generated by Django 4.0.4 on 2022-08-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='thumb',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]