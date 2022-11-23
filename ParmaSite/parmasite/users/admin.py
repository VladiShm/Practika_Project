from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.db import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('SecondName', 'FirstName',)

    search_fields = ('SecondName', 'FirstName', 'LastName')

admin.site.register(User)