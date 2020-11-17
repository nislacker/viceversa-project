# Generated by Django 3.1.3 on 2020-11-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
