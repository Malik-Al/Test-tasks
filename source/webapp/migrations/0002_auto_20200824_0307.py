# Generated by Django 2.2 on 2020-08-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
