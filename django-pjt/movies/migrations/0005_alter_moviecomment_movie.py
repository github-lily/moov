# Generated by Django 4.2.16 on 2024-11-21 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie'),
        ),
    ]
