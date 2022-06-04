from django.urls import path,include
from . import views
from . import feed
from . import feed_for_aajtk
from . import cleanupfunction



urlpatterns = [

    path('nextrandom/', views.getNextrandom),
    path('nextrandomforaajtk/', views.getNextrandom_for_aajtk),
    path('gettitle/', views.getTitle),
    path('gettitlefromaajtk/', views.getTitle_from_aajtk),
    path('savevideo/', views.savevideourl),
    path('savevideoofaajtk/', views.savevideourl_of_aajtk),
    path('feed/', feed.Videofeed()),
    path('feedforaajtk/', feed_for_aajtk.Videofeed()),
    path('clean/', cleanupfunction.cleanupFunction)

    # path('test/', views.test),


]