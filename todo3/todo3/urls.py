"""todo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from todo3 import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('remove_item/<int:idx>/', views.remove_item, name='remove_item'),
    path('favorite_item/<int:idx>/', views.favorite_item, name='favorite_item'),
    path('done_item/<int:idx>/', views.done_item, name='done_item'),
    path('mark_item/<int:idx>/', views.mark_item, name='mark_item'),
    path('update_item/<int:idx>/', views.update_item, name='update_item'),
    path('data_update_form/<int:idx>/', views.data_update_form, name='data_update_form'),
    path('testbase/', views.testbase, name='testbase'),
    path('editcat/', views.editcat, name='editcat'),
    path('remove_cat/<int:idx>/', views.remove_cat, name='remove_cat'),
    #path('testform/', views.testform, name='testform'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)