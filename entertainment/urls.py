from django.urls import path
from . import views,cleanupfunction



urlpatterns = [

    # path('videoupload/', views.VideoUpload.as_view()),
    path('clean/', cleanupfunction.cleanupfunction),
    path('savevideo/', views.savevideourl),



]