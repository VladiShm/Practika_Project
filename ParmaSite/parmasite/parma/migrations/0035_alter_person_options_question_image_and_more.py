# Generated by Django 4.1.1 on 2022-12-07 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0034_alter_discriptionquestion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['FirstName', 'SecondName'], 'verbose_name': 'статистику', 'verbose_name_plural': 'Статистика'},
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default=0, upload_to='static/', verbose_name='Картинка для теста'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 10, 49, 26, 369377), verbose_name='Дата завершения теста'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 10, 49, 26, 369377), verbose_name='Дата публикации'),
        ),
    ]