# Generated by Django 2.2.6 on 2019-11-25 08:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0016_auto_20191125_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 8, 58, 7, 586958, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]
