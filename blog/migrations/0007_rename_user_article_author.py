# Generated by Django 4.0.4 on 2022-08-02 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_author_article_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='author',
        ),
    ]
