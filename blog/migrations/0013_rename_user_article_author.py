# Generated by Django 4.0.4 on 2022-08-02 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user',
            new_name='author',
        ),
    ]
