# Generated by Django 4.1.3 on 2022-11-23 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0014_alter_question_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 10, 7, 38, 121435), verbose_name='Дата публикации'),
        ),
    ]
