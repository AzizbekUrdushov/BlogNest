# Generated by Django 4.2.16 on 2025-02-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_reaction_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblog',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textblog',
            name='fire_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textblog',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textblog',
            name='love_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='textblog',
            name='sad_count',
            field=models.IntegerField(default=0),
        ),
    ]
