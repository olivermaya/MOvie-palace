# Generated by Django 4.0.4 on 2022-06-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_actors_alter_movie_awards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='BoxOffice',
            field=models.CharField(default='N.A', help_text='A box office profit', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Production',
            field=models.CharField(default='N.A', help_text='some production data', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Ratings',
            field=models.CharField(default='N.A', help_text='A movie title', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Website',
            field=models.URLField(default='N.A', help_text='movies website url', max_length=255),
        ),
    ]