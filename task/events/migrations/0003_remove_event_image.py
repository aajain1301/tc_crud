# Generated by Django 2.1.5 on 2019-05-31 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_organiser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]