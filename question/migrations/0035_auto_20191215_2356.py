# Generated by Django 3.0 on 2019-12-15 20:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0002_auto_20191203_1815'),
        ('question', '0034_auto_20191215_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 20, 56, 16, 997110, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='Answer_dislike', to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Answer_like', to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 15, 20, 56, 16, 994909, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='Article_dislike', to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Article_like', to='userprofile.UserProfile'),
        ),
    ]
