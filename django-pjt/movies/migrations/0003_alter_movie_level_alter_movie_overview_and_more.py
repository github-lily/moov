# Generated by Django 4.2.16 on 2024-11-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movie_user_alter_movie_like_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='level',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]