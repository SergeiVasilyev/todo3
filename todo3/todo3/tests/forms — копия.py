from django import forms
from django.db import models
from .models import Todolist, TodoCat
from django.forms import ModelForm, widgets, TextInput, CheckboxInput

from .fields import ListTextWidget


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
            }),
            'category': forms.Select(attrs={
                'class': 'btn dropdown-toggle mb-2',
                'id': 'cat_items',
            }),

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
        print('!!!!!!!!!!! ', self.fields['name'])
        self.fields['name'].required = False
        



class FormForm(ModelForm):
    class Meta:
        model = TodoCat
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'enter category'
            }),
        }

    #char_field_with_list = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        _country_list = kwargs.pop('data_list', None)
        super(FormForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        print('!!!!!!!!!!! ', self.fields['name'])

        # the "name" parameter will allow you to use the same widget more than once in the same
        # form, not setting this parameter differently will cuse all inputs display the
        # same list.
        self.fields['name'].widget = ListTextWidget(data_list=_country_list, name='country-list')

    # def clean(self):
    #     super(FormForm, self).clean()
    #     username = self.cleaned_data['name']
    #     if TodoCat.objects.exclude(pk=self.instance.pk).filter(name=username).exists():
    #         raise forms.ValidationError(f'Username "{username}" is already in use.')
    #     return username