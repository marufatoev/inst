# Generated by Django 4.0.4 on 2022-08-02 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_user_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='author',
        ),
    ]
