# Generated by Django 3.2.25 on 2024-06-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('oner', models.BooleanField()),
                ('speechiness', models.IntegerField()),
                ('liveness', models.IntegerField()),
                ('acousticness', models.IntegerField()),
                ('energy', models.IntegerField()),
                ('valence', models.IntegerField()),
                ('danceability', models.IntegerField()),
                ('mode', models.IntegerField()),
                ('key', models.IntegerField()),
                ('bpm', models.IntegerField()),
            ],
        ),
    ]
