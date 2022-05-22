from django.urls import path,include
from . import views
from . import feed



urlpatterns = [

    path('nextrandom/', views.getNextrandom),
    path('gettitle/', views.getTitle),
    path('gettitlefromaajtk/', views.getTitle_from_aajtk),
    path('savevideo/', views.savevideourl),
    path('feed/', feed.Videofeed()),

    # path('test/', views.test),


]