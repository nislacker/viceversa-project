# Generated by Django 3.1.3 on 2020-11-17 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]