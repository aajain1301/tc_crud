# Generated by Django 2.1.5 on 2019-06-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190531_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]