# Generated by Django 3.0.3 on 2023-07-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0007_auto_20230719_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content_start',
            field=models.CharField(blank=True, default='', help_text='黄金5秒开头文案', max_length=200, null=True, verbose_name='开头文案'),
        ),
        migrations.AlterField(
            model_name='task',
            name='content_start_json',
            field=models.TextField(blank=True, default='', help_text='黄金5秒开头文案json', null=True, verbose_name='开头文案'),
        ),
    ]