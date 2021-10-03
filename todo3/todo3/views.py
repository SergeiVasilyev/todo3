from django.shortcuts import render, redirect

from .forms import TodolistForm
from .models import Todolist



def index(request):
   error = ''
   if request.method == 'POST':
      form = TodolistForm(request.POST)
      if form.is_valid():
         print('REQUEST:: ', form)
         form.save()
         return redirect('home')
      else:
         error = 'ERROR'

   # todos = Todolist.objects.all()
   todos = Todolist.objects.order_by('-id') # lajittelu kohteet päinvastaisessa järjestyksessä 
   form = TodolistForm()
   
   context = {
      'form': form,
      'alltodos': todos
   }
   return render(request, 'todo3/index.html', context)
   #return render(request, 'todo3/index.html', {'form': form, 'alltodos': todos})
   #return render(request, 'todo3/index.html', {'alltodos': todos})

def remove_item(request, id):
   item = Todolist.objects.get(id=id)
   item.delete()
   return redirect('home')