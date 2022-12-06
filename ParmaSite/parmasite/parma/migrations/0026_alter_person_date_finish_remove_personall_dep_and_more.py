# Generated by Django 4.1.1 on 2022-12-06 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0025_remove_person_image_alter_person_date_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 17, 1, 44, 604240), verbose_name='Дата завершения теста'),
        ),
        migrations.RemoveField(
            model_name='personall',
            name='dep',
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 17, 1, 44, 604987), verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='personall',
            name='dep',
            field=models.ManyToManyField(to='parma.person'),
        ),
    ]
