
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

menu = ["О сайте", "Войти", "Тесты"]

def index(request):
    people = Person.objects.all()
    return render(request, 'parma/index.html', {'people':people,'menu': menu, 'title': 'Parma'})
def test(request):
    question = Question.objects.all()
    return render(request, 'parma/test.html', {'questions': question, })


