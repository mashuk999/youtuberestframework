"""projectYoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from entertainment import views
from entertainment import feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entertainx/', views.getNextrandom),
    path('gettitle/', views.getTitle),
    path('download/', views.downloadvideofromheroku),
    path('download2/', views.downloadvideofromheroku2),
    path('videoupload/', views.VideoUpload.as_view()),
    path('videouploadwithcloudinary/', views.VideoUploadWithCloudinary.as_view()),
    path('feed/', feed.Videofeed()),

    path('api-auth/', include('rest_framework.urls')),

]
