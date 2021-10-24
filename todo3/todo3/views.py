from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect


from .forms import TodolistForm, TodoCatForm
from .models import Todolist, TodoCat
from .forms import FormForm

def index(request):
   cats = TodoCat.objects.order_by('-id')
   form_cat = FormForm(data_list=cats)
   category = None
   if request.method == 'POST':
      form_cat = FormForm(request.POST)
      print('request.POST.get("name") ', request.POST.get("name"))
      if form_cat.is_valid() and request.POST.get("name"): # срабатывает если значение новое, а не из базы данных
         print('is_valid = VALID')
         print('form_cat.cleaned_data["name"]:: ', form_cat.cleaned_data['name']) # иначе добовляем новую категорию
         category = form_cat.save() # записываем новое значение в переменную как инстанс TodoCat
         print('category ', category)
      elif request.POST.get("name") and not category: # Если значение выбирается из БД, то 
         category = TodoCat.objects.get(name=request.POST.get("name")) # Ищем существующую категорию и записываем в переменную как инстанс TodoCat
         print('item', category)
      else:
         category = None # Присвоить None переменной можно, но может быть продумать значение по умолчанию
         error = 'ERROR'
         #print(error)
         return redirect('home')

      form = TodolistForm(request.POST)
      if form.is_valid():
         print('REQUEST2 form.is_valid:: ', request.POST.get("name"))
         todo_item = form.save(commit=False)
         todo_item.category = category # Можно передать значение только через инстанс TodoCat, так как он указан в моделе Todolist ...ForeignKey(TodoCat...
         todo_item.save()
         #form.save()
         return redirect('home')
      else:
         error = 'ERROR'

   alltodos = Todolist.objects.order_by('-id') # lajittelu kohteet päinvastaisessa järjestyksessä 
   form = TodolistForm()
   categories = TodoCat.objects.order_by('name') 
   context = {
      'form': form,
      'form_cat': form_cat,
      'alltodos': alltodos,
      'categories': categories
   }

   return render(request, 'todo3/index.html', context)


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
   item = Todolist.objects.get(id=idx) # SELECT * FROM Todolist WHERE id=idx
   if not item.todoitem_done:
      item.todoitem_done = True
   else:
      item.todoitem_done = False
   item.save()
   return redirect('home')

@csrf_exempt
def mark_item(request, idx):
   item = Todolist.objects.get(id=idx) # SELECT * FROM Todolist WHERE id=idx
   if not item.todoitem_fav:
      item.todoitem_fav = True
   else:
      item.todoitem_fav = False
   item.save()
   #print(item.todoitem_fav)
   return HttpResponse(item.todoitem_fav)

@csrf_exempt
def update_item (request, idx):
   print('idx ', idx)
   item = Todolist.objects.get(id=idx) # SELECT * FROM Todolist WHERE id=idx
   print('item ', item.todoitem)
   
   form = TodolistForm(request.POST) # Saamme tietoja FORM elementistä
   if form.is_valid():
      print('REQUEST:: ', form.cleaned_data['todoitem']) 
      
      # Vaihdamme saadut arvot tietokannassa
      item.todoitem = form.cleaned_data['todoitem'] # cleaned_data kautta voimme saada tietoja erikseen 
      item.todo_description = form.cleaned_data['todo_description']
      item.save()
   return redirect('home')

def data_update_form (request, idx):
   item = Todolist.objects.get(id=idx)
   data = {'todoitem': item.todoitem, 'todo_description': item.todo_description}
   return JsonResponse(data)

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



def editcat (request):
   categories = TodoCat.objects.order_by('name') 
   context = {
      'categories': categories,
   }
   return render(request, 'todo3/category_manage.html', context)

def remove_cat(request, idx):
   item = TodoCat.objects.get(id=idx)
   item.delete()
   return redirect('editcat')
