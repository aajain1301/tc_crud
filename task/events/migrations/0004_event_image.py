# Generated by Django 2.1.5 on 2019-05-31 19:30

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
            preserve_default=False,
        ),
    ]
