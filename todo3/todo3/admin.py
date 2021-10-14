from django.contrib import admin

from .models import Todolist

#@admin.register(Todolist)

class TodolistAdmin(admin.ModelAdmin):
    fields = ["todoitem", "todoitem_fav", "todoitem_done", "todo_description"]


admin.site.register(Todolist, TodolistAdmin)