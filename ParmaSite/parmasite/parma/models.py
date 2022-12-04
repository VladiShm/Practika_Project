from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class Person(models.Model):
    FirstName = models.CharField(max_length=100, verbose_name="Имя")
    SecondName = models.CharField(max_length=100, verbose_name="Фамилия")
    LastName = models.CharField(max_length=100, verbose_name="Отчество")
    Departament = models.CharField(max_length=100, verbose_name="Департамент")
    Login = models.CharField(max_length=100, verbose_name='Логин')
    Password = models.CharField(max_length=100, verbose_name='Пароль')
    success = models.BooleanField(default=False)

    def __str__(self):
        return self.FirstName

    class Meta:
        verbose_name = "сотрудника компании"
        verbose_name_plural = "Сотрудники компании"
        ordering = ['FirstName', 'SecondName', 'LastName']


class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=400, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата публикации", default=datetime.datetime.now())
    is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
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
    q1 = models.ManyToManyField(Question)
    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
