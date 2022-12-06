# Generated by Django 4.1.1 on 2022-12-06 10:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0021_alter_person_options_person_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 15, 9, 17, 779051), verbose_name='Дата завершения теста'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Визуальное представление статистики'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 15, 9, 17, 780051), verbose_name='Дата публикации'),
        ),
        migrations.CreateModel(
            name='DiscriptionQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discription', models.CharField(max_length=500, verbose_name='Описание ответа на вопрос теста')),
                ('Name_Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parma.question')),
            ],
        ),
    ]