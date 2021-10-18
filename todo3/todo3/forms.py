from django.db import models
from .models import Todolist, TodoCat
from django.forms import ModelForm, widgets, TextInput, CheckboxInput


class TodolistForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ['todoitem', 'todoitem_fav', 'todoitem_done', 'todo_description', 'category']
        widgets = {
            'todoitem': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'enter text'
            }),
            'todoitem_fav': CheckboxInput(attrs={
                'class': 'form-check-input mb-2'
            }),
            'todo_description': widgets.Textarea(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'enter description'
            })
        }

class TodoCatForm(ModelForm):
    class Meta:
        model = TodoCat
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'enter category'
            }),
        }

    # https://stackoverflow.com/questions/24045135/django-make-certain-fields-in-a-modelform-required-false
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
