from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [

    path('entertainx/', views.getNextrandom),
    path('gettitle/', views.getTitle),
    path('videouploadwithcloudinary/', views.savevideourl),
    # path('test/', views.test),


]