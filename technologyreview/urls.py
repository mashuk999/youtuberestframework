from django.urls import path
from . import views




urlpatterns = [


    path('gettitle/', views.getTitle),
    path('nextrandom/', views.getNextrandom),
    path('savevideo/', views.savevideourl),



]