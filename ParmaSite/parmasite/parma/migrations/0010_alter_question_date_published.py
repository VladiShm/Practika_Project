# Generated by Django 4.1.3 on 2022-11-22 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0009_alter_question_date_published_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 21, 14, 16, 221925), verbose_name='Дата публикации'),
        ),
    ]
