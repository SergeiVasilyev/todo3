from django.contrib import admin

from .models import Todolist, TodoCat

#@admin.register(Todolist)

class TodolistAdmin(admin.ModelAdmin):
    fields = ["todoitem", "todoitem_fav", "todoitem_done", "todo_description", "category"]

class TodoCatAdmin(admin.ModelAdmin):
    fields = ["name"]


admin.site.register(Todolist, TodolistAdmin)
admin.site.register(TodoCat)