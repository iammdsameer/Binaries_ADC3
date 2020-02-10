# Generated by Django 3.0.2 on 2020-02-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_remove_musics_music_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='image',
            field=models.CharField(default='https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fclipart-library.com%2Fimg%2F870190.png&f=1&nofb=1', max_length=2083, verbose_name="Artist's Image"),
        ),
        migrations.AlterField(
            model_name='artists',
            name='name',
            field=models.CharField(default='Unknown', max_length=250, verbose_name="Artist's Name"),
        ),
        migrations.AlterField(
            model_name='distributors',
            name='logo',
            field=models.CharField(default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmdbootstrap.com%2Fimg%2FPhotos%2FOthers%2Fplaceholder-avatar.jpg&f=1&nofb=1', max_length=2083, verbose_name="Distributor's Logo"),
        ),
        migrations.AlterField(
            model_name='distributors',
            name='name',
            field=models.CharField(default='Unknown', max_length=250, verbose_name="Distributor's Name"),
        ),
    ]
