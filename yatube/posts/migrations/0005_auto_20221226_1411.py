# Generated by Django 2.2.19 on 2022-12-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221226_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=18, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.TextField(max_length=50, verbose_name='Название'),
        ),
    ]
