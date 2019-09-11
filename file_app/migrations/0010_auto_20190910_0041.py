# Generated by Django 2.2.4 on 2019-09-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0009_auto_20190910_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='filedata',
            name='avg_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='avg_max_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='avg_min_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='file_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='filedata',
            name='max_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='max_temp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='mean_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='min_humd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filedata',
            name='min_temp',
            field=models.IntegerField(default=0),
        ),
    ]
