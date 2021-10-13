from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse


from .forms import TodolistForm
from .models import Todolist


def index(request):
   error = ''
   if request.method == 'POST':
      form = TodolistForm(request.POST)
      if form.is_valid():
         print('REQUEST:: ', form.base_fields)
         form.save()
         return redirect('home')
      else:
         error = 'ERROR'

   # todos = Todolist.objects.all()
   todos = Todolist.objects.order_by('-id') # lajittelu kohteet päinvastaisessa järjestyksessä 
   form = TodolistForm()
   
   class_highlight = {'true': 'list-group-item-light', 'false': 'list-group-item-success'}

   context = {
      'form': form,
      'alltodos': todos,
      'class_highlight': class_highlight
   }
   return render(request, 'todo3/index.html', context)
   #return render(request, 'todo3/index.html', {'form': form, 'alltodos': todos})
   #return render(request, 'todo3/index.html', {'alltodos': todos})

def remove_item(request, idx):
   item = Todolist.objects.get(id=idx)
   item.delete()
   return redirect('home')

def favorite_item(request, idx):
   item = Todolist.objects.get(id=idx)
   if not item.todoitem_fav:
      item.todoitem_fav = True
   else:
      item.todoitem_fav = False
   item.save()
   return redirect('home')

def done_item(request, idx):
   item = Todolist.objects.get(id=idx)
   if not item.todoitem_done:
      item.todoitem_done = True
   else:
      item.todoitem_done = False
   item.save()
   return redirect('home')

@csrf_exempt
def mark_item(request, idx):
   item = Todolist.objects.get(id=idx)
   if not item.todoitem_fav:
      item.todoitem_fav = True
      res = 'list-group-item-success'
   else:
      item.todoitem_fav = False
      res = 'list-group-item-light'
   item.save()
   #print(item.todoitem_fav)
   return HttpResponse(res)

def update_item (request, idx):
   print('idx ', idx)
   item = Todolist.objects.get(id=idx)
   print('item ', item.todoitem)
   form = TodolistForm(request.POST)
   if form.is_valid():
      print('REQUEST:: ', form.cleaned_data['todoitem'])
      el_todoitem = form.cleaned_data['todoitem']
      # rec = Todolist(todoitem=el_todoitem, todoitem_fav=item.todoitem_fav, todoitem_done=item.todoitem_done)
      item.todoitem = el_todoitem
      item.save()
   return redirect('home')

def testbase (request):
   error = ''
   if request.method == 'POST':
      form = TodolistForm(request.POST)
      if form.is_valid():
         print('REQUEST:: ', form.base_fields)
         form.save()
         return redirect('home')
      else:
         error = 'ERROR'
   form = TodolistForm()
   return render(request, 'todo3/test2.html', {'form': form}) 



# def chek_fav(args):
#    class_highlight = {'true': 'list-group-item-light', 'false': 'list-group-item-warning'}
#    if args:
#       return class_highlight.true
#    else:
#       return class_highlight.false