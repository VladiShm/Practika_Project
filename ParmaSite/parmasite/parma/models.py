from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class Person(models.Model):
    FirstName = models.CharField(max_length=100, verbose_name="Имя")
    SecondName = models.CharField(max_length=100, verbose_name="Фамилия")
    Departament = models.CharField(max_length=100, verbose_name="Департамент")
    Sucsess = models.IntegerField(verbose_name = "Успешность прохождения теста в %")
    Date_finish = models.DateTimeField(verbose_name="Дата завершения теста", default=datetime.datetime.now())

    def __str__(self):
        return self.FirstName

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"
        ordering = ['FirstName', 'SecondName',]




class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=400, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата публикации", default=datetime.datetime.now())
    is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавить новый вопрос'
        verbose_name_plural = 'Добавить новый вопрос'


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Test(models.Model):
    test_name = models.CharField(max_length=200, verbose_name="Имя теста")
    q1 = models.ManyToManyField(Question, verbose_name="Вопросы")


    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Добавить новый тест'
        verbose_name_plural = 'Добавить новый тест'



class DiscriptionQuestion(models.Model):
    Name_Question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name = "Вопрос")
    Discription = models.CharField(max_length = 500, verbose_name = "Описание ответа на вопрос теста")



    class Meta:
        verbose_name = 'Комментарии к правильному ответу на вопрос теста'
        verbose_name_plural = 'Комментарии к правильному ответу на вопрос теста'
