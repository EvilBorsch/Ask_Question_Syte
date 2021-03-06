# Generated by Django 2.2.6 on 2019-11-27 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0021_auto_20191127_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 18, 47, 20, 173990, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 18, 47, 20, 171867, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]
