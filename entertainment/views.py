# from django.shortcuts import render,HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from entertainment import processArticle
from .models import *
from .serializer import Entertainmentserializer,SaveVideoserializer
import datetime,random
import xmltodict
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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
        serializer = SaveVideoserializer(data=request.data  )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)