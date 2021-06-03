from django.urls import path
from . import views,techno_feed





urlpatterns = [


    path('gettitle/', views.getTitle),
    path('nextrandom/', views.getNextrandom),
    path('savevideo/', views.savevideourl),
    path('feed/', techno_feed.Videofeed()),



]