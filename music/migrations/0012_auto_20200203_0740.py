# Generated by Django 3.0.2 on 2020-02-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20200203_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='artist',
        ),
        migrations.AddField(
            model_name='albums',
            name='year',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]