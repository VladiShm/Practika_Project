from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.db import models
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','last_name', 'email')


admin.site.register(User, UserAdmin)