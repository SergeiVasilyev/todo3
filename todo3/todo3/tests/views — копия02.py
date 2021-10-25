from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect


from .forms import TodolistForm, TodoCatForm
from .models import Todolist, TodoCat


def index(request):
   error = ''
   if request.method == 'POST':
      form = TodolistForm(request.POST)
      cat = TodoCatForm(request.POST)
      #print('REQUEST:: ', form.base_fields)
      if cat.is_valid() and cat.cleaned_data['name']:
         category = cat.save()
      else:
         category = None
      if form.is_valid(): 
         print('REQUEST:: ', form.cleaned_data['category'])
         # Переделать форин кей, соеденить с ID
         # django form change field value
         # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
         if category:
            todo_item = form.save(commit=False)
            todo_item.category = category
            todo_item.save()
         else:
            form.save()
         
         return redirect('home')
      else:
         error = 'ERROR'

   # todos = Todolist.objects.all()
   todos = Todolist.objects.order_by('-id') # lajittelu kohteet päinvastaisessa järjestyksessä 
   form = TodolistForm()
   cat = TodoCatForm()

   context = {
      'form': form,
      'cat': cat,
      'alltodos': todos,
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



# def chek_fav(args):
#    class_highlight = {'true': 'list-group-item-light', 'false': 'list-group-item-warning'}
#    if args:
#       return class_highlight.true
#    else:
#       return class_highlight.false


from .forms import FormForm

def testform(request):
   # instead of hardcoding a list you could make a query of a model, as long as
   # it has a __str__() method you should be able to display it.
   country_list = ('Mexico', 'USA', 'China', 'France')
   cats = TodoCat.objects.order_by('-id')
   form = FormForm(data_list=cats)
   if request.method == 'POST':
      try:
         testitem = TodoCat.objects.get(name=request.POST.get("name")) # если нет объекта, то проверяем на ошибку
      except:
         testitem = ''
      # Проверяем, если категория существует, то не сохраняем объект, не получаем ошибки, а переходим к сохранению потом Todolist с этой category ID
      #print(request.POST.get("name"))
      if not testitem:
         form = FormForm(request.POST)
         if form.is_valid():
            try:
               item = Todolist.objects.get(name=form.cleaned_data['name']) # если существует иакая каиегория, то перезагружаем страницу
               return redirect('testform')
            except:
               print('REQUEST:: ', form.cleaned_data['name']) # иначе добовляем новую категорию
               form.save()
               return redirect('testform')
         else:
            error = 'ERROR'
   return render(request, 'todo3/testform.html', {
      'form': form
   })




# def chek_fav(args):
#    class_highlight = {'true': 'list-group-item-light', 'false': 'list-group-item-warning'}
#    if args:
#       return class_highlight.true
#    else:
#       return class_highlight.false




# def testform(request):
#    # instead of hardcoding a list you could make a query of a model, as long as
#    # it has a __str__() method you should be able to display it.
#    country_list = ('Mexico', 'USA', 'China', 'France')
#    cats = TodoCat.objects.order_by('-id')
#    form = FormForm(data_list=cats)
#    if request.method == 'POST':
#       try:
#          testitem = TodoCat.objects.get(name=request.POST.get("name")) # если нет объекта, то проверяем на ошибку
#       except:
#          testitem = ''
#       # Проверяем, если категория существует, то не сохраняем объект, не получаем ошибки, а переходим к сохранению потом Todolist с этой category ID
#       #print(request.POST.get("name"))
#       if not testitem:
#          form = FormForm(request.POST)
#          if form.is_valid():
#             try:
#                item = Todolist.objects.get(name=form.cleaned_data['name']) # если существует иакая каиегория, то перезагружаем страницу
#                return redirect('testform')
#             except:
#                print('REQUEST:: ', form.cleaned_data['name']) # иначе добовляем новую категорию
#                form.save()
#                return redirect('testform')
#          else:
#             error = 'ERROR'
#    return render(request, 'todo3/testform.html', {
#       'form': form
#    })

# def index(request):
#    error = ''
#    if request.method == 'POST':
#       form = TodolistForm(request.POST)
#       cat = TodoCatForm(request.POST)
#       #print('REQUEST:: ', form.base_fields)
#       if cat.is_valid() and cat.cleaned_data['name']:
#          category = cat.save()
#       else:
#          category = None
#       if form.is_valid(): 
#          print('REQUEST:: ', form.cleaned_data['category'])
#          # Переделать форин кей, соеденить с ID
#          # django form change field value
#          # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

#          # item = TodoCat.objects.get(name='nEW')
#          # print(item)
#          if category:
#             todo_item = form.save(commit=False)
#             todo_item.category = category
#             todo_item.save()
#          else:
#             form.save()
         
#          return redirect('home')
#       else:
#          error = 'ERROR'

#    # todos = Todolist.objects.all()
#    todos = Todolist.objects.order_by('-id') # lajittelu kohteet päinvastaisessa järjestyksessä 
#    form = TodolistForm()
#    cat = TodoCatForm()

#    context = {
#       'form': form,
#       'cat': cat,
#       'alltodos': todos,
#    }
#    return render(request, 'todo3/index.html', context)