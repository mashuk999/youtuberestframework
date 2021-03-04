# from django.shortcuts import render,HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import Entertainmentserializer



@csrf_exempt
def hello(request):
    if request.method=='GET':
        latestdata = Entertainmentdb.objects.latest('id')
        serializers = Entertainmentserializer(latestdata)
        return JsonResponse(serializers.data, safe=False)
    if request.method=='POST':
       title=request.POST.get('title')
       date=request.POST.get('date')
       obj=Entertainmentdb(title=title,date=date)
       obj.save()
       latestdata = Entertainmentdb.objects.latest('id')
       serializers = Entertainmentserializer(latestdata)
       return JsonResponse(serializers.data, safe=False)


    return HttpResponse('ok')

# Create your views here.
