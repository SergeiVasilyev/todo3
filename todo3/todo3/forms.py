from django.db import models
from .models import Todolist
from django.forms import ModelForm, widgets, TextInput, CheckboxInput


class TodolistForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ['todoitem', 'todoitem_fav', 'todoitem_done']
        widgets = {
            'todoitem': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Syötä tehtävä'
            }),
            'todoitem_fav': CheckboxInput(attrs={
                'class': 'form-check-input mb-2'
            })
        }