from django.contrib import admin
from .models import *
from import_export import fields
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.widgets import ForeignKeyWidget

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person


class PersonAdmin(ImportExportActionModelAdmin):
    resource_class = PersonResource
    list_display = ('SecondName', 'FirstName', 'Departament','Sucsess', 'Date_finish' )

    search_fields = ('SecondName', 'FirstName', )


admin.site.register(Person, PersonAdmin)

admin.site.site_title = 'Личный кабинет администратора'
admin.site.site_header = 'Личный кабинет администратора'



class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active')
    search_fields =('title', 'date_published',)
    inlines = [AnswerInline]

class TestAdmin(admin.ModelAdmin):
    search_fields = ('test_name',)

admin.site.register(Test, TestAdmin)

admin.site.register(Question, QuestionAdmin)

class DiscriptionQuestionAdmin(admin.ModelAdmin):
    list_display = ('Name_Question', 'Discription')
    search_fields = ('Name_Question',)


admin.site.register(DiscriptionQuestion, DiscriptionQuestionAdmin)

class MyAdmin(admin.ModelAdmin):
    def log_addition(self, *args):
            return
    def log_change(self, *args):
            return
    def log_deletion(self, *args):
            return