# Generated by Django 4.1.3 on 2022-11-19 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0007_alter_question_date_published_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 19, 22, 29, 40, 951381), verbose_name='Дата публикации'),
        ),
    ]