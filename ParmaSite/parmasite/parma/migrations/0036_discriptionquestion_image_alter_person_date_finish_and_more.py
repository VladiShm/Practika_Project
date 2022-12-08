# Generated by Django 4.1.1 on 2022-12-08 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0035_alter_person_options_question_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discriptionquestion',
            name='image',
            field=models.ImageField(default=0, upload_to='static/', verbose_name='Загрузите изображение - пояснение к вопросу'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 0, 16, 52, 566521), verbose_name='Дата завершения теста'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 0, 16, 52, 567519), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(upload_to='static/', verbose_name='Загрузите вспомогательное изображение для вопроса'),
        ),
    ]
