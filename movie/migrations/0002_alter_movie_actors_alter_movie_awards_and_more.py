# Generated by Django 4.0.4 on 2022-06-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.CharField(default='N.A', help_text='Actors', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.CharField(blank=True, help_text='movie awards', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(default='N.A', help_text='movie country', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(blank=True, help_text='directors', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Genre',
            field=models.CharField(default='N.A', help_text='genres', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Language',
            field=models.CharField(blank=True, help_text='language', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Metascore',
            field=models.IntegerField(default='N.A', help_text='Meta score', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Plot',
            field=models.CharField(default='N.A', help_text='plot', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Rated',
            field=models.CharField(default='N.A', help_text='movies rating', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.CharField(default='N.A', help_text='movie released time', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(default='N.A', help_text='total runtime', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Title',
            field=models.CharField(help_text='A movie title', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.CharField(default='N.A', help_text='writters', max_length=255),
        ),
    ]
