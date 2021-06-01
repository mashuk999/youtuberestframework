from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from entertainment.serializer import *
from . import techno_processArticle
import datetime,random
from.models import *


@csrf_exempt
def getNextrandom(request):
    if request.method=='GET':
        latestdata = Technodb.objects.latest('id')
        serializers = Technologyserializer(latestdata)
        return JsonResponse(serializers.data, safe=False)
    return HttpResponse('ok')



def getTitle(request):
    if request.method=='GET':
        title, summary, content, YTtitle = techno_processArticle.findArticle()
        data={
            'title':title,
            'summary':summary,
            'content':content,
            'Ytitle':YTtitle
        }
        nextran = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta( minutes=random.randrange(245, 350)))
        nextran = nextran[:19]
        nextran=(datetime.datetime.strptime(nextran,"%Y-%m-%d %H:%M:%S"))
        obj=Technodb(title=title,nextrandom=nextran)
        obj.save()
        return JsonResponse(data,safe=False)



@csrf_exempt
def savevideourl(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        videopublicid = request.POST.get('videoPublicId')
        videourl = request.POST.get('videoUrl')
        obj = SaveVideo_technology(title=title, videoPublicId=videopublicid, videoUrl=videourl)
        obj.save()

        print('save in db')
        return HttpResponse('done')
    else:
        print('video not saved')