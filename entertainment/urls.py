from django.urls import path
from . import views,cleanupfunction,entertain_feed



urlpatterns = [

    # path('videoupload/', views.VideoUpload.as_view()),
    path('clean/', cleanupfunction.cleanupfunction),
    path('savevideo/', views.savevideourl),
    path('feed/', entertain_feed.Videofeed()),



]