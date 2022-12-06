# Generated by Django 4.1.1 on 2022-12-06 11:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parma', '0023_alter_discriptionquestion_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discriptionquestion',
            name='Name_Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parma.question', verbose_name='Название теста'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Date_finish',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 16, 24, 6, 803542), verbose_name='Дата завершения теста'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 16, 24, 6, 803542), verbose_name='Дата публикации'),
        ),
    ]
