# Generated by Django 4.0.4 on 2022-07-29 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]