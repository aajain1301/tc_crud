# Generated by Django 2.1.5 on 2019-06-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190602_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics', verbose_name='image'),
        ),
    ]
