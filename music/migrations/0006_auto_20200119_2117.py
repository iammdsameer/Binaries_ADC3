# Generated by Django 3.0.2 on 2020-01-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200116_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='music_file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
