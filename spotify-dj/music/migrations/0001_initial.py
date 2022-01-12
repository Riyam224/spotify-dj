# Generated by Django 3.2.7 on 2021-09-07 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='album')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Musoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('artist', models.CharField(max_length=50, verbose_name='artist')),
                ('time_length', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='time length')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='musics')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='cover image ')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.album')),
            ],
            options={
                'verbose_name': 'Musoc',
                'verbose_name_plural': 'Musocs',
            },
        ),
    ]
