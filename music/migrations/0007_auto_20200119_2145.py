# Generated by Django 3.0.2 on 2020-01-19 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200119_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='musics',
            name='music_album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Albums'),
        ),
        migrations.AddField(
            model_name='musics',
            name='music_genre',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Generes'),
        ),
    ]
