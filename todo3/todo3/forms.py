from django.db import models
from .models import Todolist
from django.forms import ModelForm, widgets, TextInput, CheckboxInput


class TodolistForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ['todoitem', 'todoitem_fav', 'todoitem_done', 'todo_description']
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