# Generated by Django 3.0 on 2019-12-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0002_auto_20191203_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='question/static/question/base/default.jpeg',
                                    upload_to='question/static/images/avatars', verbose_name='Изображение'),
        ),
    ]
