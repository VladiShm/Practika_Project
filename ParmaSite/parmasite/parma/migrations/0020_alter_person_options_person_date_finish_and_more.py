# Generated by Django 4.1.1 on 2022-12-06 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0019_alter_person_options_alter_question_date_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['FirstName', 'SecondName', 'LastName'], 'verbose_name': 'Статистика сотрудника компании', 'verbose_name_plural': 'Статистика сотрудники компании'},
        ),
        migrations.AddField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 14, 40, 32, 565624), verbose_name='Дата завершения теста'),
        ),
        migrations.AddField(
            model_name='person',
            name='Sucsess',
            field=models.IntegerField(default=0, verbose_name='Успешность прохождения теста в %'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 14, 40, 32, 566622), verbose_name='Дата публикации'),
        ),
    ]
