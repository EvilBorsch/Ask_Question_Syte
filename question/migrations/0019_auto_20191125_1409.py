# Generated by Django 2.2.6 on 2019-11-25 14:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0018_auto_20191125_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 14, 9, 33, 501259, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
    ]
