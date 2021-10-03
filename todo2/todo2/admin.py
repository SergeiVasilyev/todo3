from django.contrib import admin

from .models import Todolist

class TodolistAdmin(admin.ModelAdmin):
    fields = ["todoitem", "todoitem_fav"]

admin.site.register(Todolist, TodolistAdmin)