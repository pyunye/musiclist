# Generated by Django 3.2.25 on 2024-06-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_artist_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
