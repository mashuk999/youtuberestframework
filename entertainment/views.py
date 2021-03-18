# from django.shortcuts import render,HttpResponse
from pathlib import Path

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from entertainment import processArticle
from .models import *
import os

from django.conf import  settings
from .serializer import Entertainmentserializer,SaveVideoserializer
import datetime,random
import xmltodict
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.static import serve


from rest_framework import generics



@csrf_exempt
def getNextrandom(request):
    if request.method=='GET':
        latestdata = Entertainmentdb.objects.latest('id')
        serializers = Entertainmentserializer(latestdata)
        return JsonResponse(serializers.data, safe=False)


    return HttpResponse('ok')



def getTitle(request):
    if request.method=='GET':
        title, summary, content, YTtitle = processArticle.findArticle()
        data={
            'title':title,
            'summary':summary,
            'content':content,
            'Ytitle':YTtitle
        }
        nextran = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta( minutes=random.randrange(245, 350)))
        nextran = nextran[:19]
        nextran=(datetime.datetime.strptime(nextran,"%Y-%m-%d %H:%M:%S"))
        obj=Entertainmentdb(title=title,nextrandom=nextran)
        obj.save()
        return JsonResponse(data,safe=False)



# def videosave(request):
#     if request.method=='POST':


class VideoUpload(generics.CreateAPIView):
    # parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated] test now
    serializer_class = SaveVideoserializer

    # def get(self,request,format=None):
    #     obj=SaveVideo.objects.all()
    #     serializer=SaveVideoserializer(obj)
    #     return Response(serializer.data)
    def post(self, request, format=None):
        serializer = SaveVideoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@csrf_exempt
def savevideourl(request):
    if request.method=='POST':
        # file = request.data.get('video')
        title = request.POST.get('title')
        videopublicid=request.POST.get('videoPublicId')
        videourl=request.POST.get('videoUrl')
        obj = SaveVideo(title=title,videoPublicId=videopublicid,videoUrl=videourl)
        obj.save()
        print('save in db')
        return HttpResponse('dome')



def downloadvideofromheroku(request):
    try:
        filepath = request.GET['urlpath']
        print(filepath)
        BASE_DIR = Path(__file__).resolve().parent.parent
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        print(MEDIA_ROOT)
        print(os.path.join(MEDIA_ROOT, filepath))

        response = HttpResponse()
        response['Content-Type'] = 'video/mp4'
        response['X-Accel-Redirect'] = os.path.join(MEDIA_ROOT,filepath)
        response['Content-Disposition'] = 'attachment;filename=' + os.path.join(MEDIA_ROOT,filepath)
    except Exception:
        raise Http404
    return response

def downloadvideofromheroku2(request):
    try:
        filepath = request.GET['urlpath']
        print(filepath)
        BASE_DIR = Path(__file__).resolve().parent.parent
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")
        print(MEDIA_ROOT)
        print(os.path.join(MEDIA_ROOT, filepath))

        from wsgiref.util import FileWrapper

        file = FileWrapper(open(os.path.join(MEDIA_ROOT,filepath), 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
        return response
    except Exception:
        raise Http404
