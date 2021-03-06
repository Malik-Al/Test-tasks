# Generated by Django 2.2 on 2020-08-24 04:31

from django.db import migrations


def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('webapp', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)


def drop_profiles(apps, schema_editor):
    Profile = apps.get_model('webapp', 'Profile')
    Profile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200824_0430'),
    ]

    operations = [
        migrations.RunPython(create_profiles, drop_profiles),
    ]
