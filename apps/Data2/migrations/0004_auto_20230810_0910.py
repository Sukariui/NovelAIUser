# Generated by Django 3.0.3 on 2023-08-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data2', '0003_auto_20230809_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietaskeach',
            name='end_time',
            field=models.CharField(default=' ', max_length=50, verbose_name='字幕结束时间'),
        ),
        migrations.AddField(
            model_name='movietaskeach',
            name='start_time',
            field=models.CharField(default=' ', max_length=50, verbose_name='字幕开始时间'),
        ),
    ]