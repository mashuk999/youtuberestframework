# from django.shortcuts import render,HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from entertainment import processArticle
from .models import *
from .serializer import Entertainmentserializer
import datetime,random
import xmltodict




@csrf_exempt
def getNextrandom(request):
    if request.method=='GET':
        latestdata = Entertainmentdb.objects.latest('id')
        serializers = Entertainmentserializer(latestdata)
        return JsonResponse(serializers.data, safe=False)
    # if request.method=='POST':
    #    title=request.POST.get('title')
    #    nextran = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=random.randrange(245, 350)))
    #    # obj=datetime.datetime.strptime(nextran,"%Y-%m-%d %H:%M:%S")
    #    ness=nextran.replace(microsecond=0)
    #    # print(type(obj))phone
    #    obj=Entertainmentdb(title=title,nextrandom=ness)
    #    obj.save()
    #    latestdata = Entertainmentdb.objects.latest('id')
    #    serializers = Entertainmentserializer(latestdata)
    #    return JsonResponse(serializers.data, safe=False)


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