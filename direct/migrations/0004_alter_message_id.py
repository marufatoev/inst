# Generated by Django 4.0.4 on 2022-08-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0003_auto_20200728_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
