# Generated by Django 2.1.2 on 2019-01-09 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='userproperty_profile',
        ),
    ]
