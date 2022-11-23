from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('SecondName', 'FirstName', 'LastName', 'Departament')

    search_fields = ('SecondName', 'FirstName', 'LastName')

#admin.site.register(Person, PersonAdmin)

admin.site.site_title = 'Личный кабинет администратора'
admin.site.site_header = 'Личный кабинет администратора'

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active')
    inlines = [AnswerInline]



admin.site.register(Question, QuestionAdmin)

class MyAdmin(admin.ModelAdmin):
    def log_addition(self, *args):
            return
    def log_change(self, *args):
            return
    def log_deletion(self, *args):
            return