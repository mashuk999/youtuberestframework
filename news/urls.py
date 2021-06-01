from django.urls import path,include
from . import views
from . import feed



urlpatterns = [

    path('nextrandom/', views.getNextrandom),
    path('gettitle/', views.getTitle),
    path('savevideo/', views.savevideourl),

    # path('test/', views.test),


]