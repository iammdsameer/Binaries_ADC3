# Generated by Django 3.0.2 on 2020-01-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200111_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music_album',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='music_artist',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_coverArt',
            field=models.CharField(default='https://i.ytimg.com/vi/5Peo-ivmupE/maxresdefault.jpg', max_length=2083),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_length',
            field=models.IntegerField(null=True),
        ),
    ]
