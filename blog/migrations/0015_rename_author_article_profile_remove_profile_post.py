# Generated by Django 4.0.4 on 2022-08-03 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_profile_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]