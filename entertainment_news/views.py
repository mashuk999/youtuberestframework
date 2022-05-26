from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import processArticle, processArticle_from_aajtk
from .models import *
from entertainment.serializer import Newsserializer, Newsserializer_for_aajtk
import datetime,random




@csrf_exempt
def getNextrandom(request):
    if request.method=='GET':
        latestdata = entertainmentNewsdb.objects.latest('id')
        serializers = Newsserializer(latestdata)
        return JsonResponse(serializers.data, safe=False)
    return HttpResponse('ok')


def getNextrandom_for_aajtk(request):
    if request.method=='GET':
        latestdata = entertainmentNewsdb_for_aajtk.objects.latest('id')
        serializers = Newsserializer_for_aajtk(latestdata)
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
        obj=entertainmentNewsdb(title=title,nextrandom=nextran)
        obj.save()
        return JsonResponse(data,safe=False)



def getTitle_from_aajtk(request):
    if request.method=='GET':
        title, content, summary, YTtitle = processArticle_from_aajtk.dataFromThearticles()
        data={
            'title':title,
            'content':content,
            'summary': summary,
            'Ytitle':YTtitle
        }
        nextran = str(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta( minutes=random.randrange(245, 350)))
        nextran = nextran[:19]
        nextran=(datetime.datetime.strptime(nextran,"%Y-%m-%d %H:%M:%S"))
        obj=entertainmentNewsdb_for_aajtk(title=title,nextrandom=nextran)
        obj.save()
        return JsonResponse(data,safe=False)




@csrf_exempt
def savevideourl(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        videopublicid = request.POST.get('videoPublicId')
        videourl = request.POST.get('videoUrl')
        obj = entertainmentSaveVideonews(title=title, videoPublicId=videopublicid, videoUrl=videourl)
        obj.save()

        print('save in db')
        return HttpResponse('done')
    else:
        print('video not saved')



@csrf_exempt
def savevideourl_of_aajtk(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        nameofvideo = request.POST.get('name')
        videourl = request.POST.get('videoUrl')
        obj = entertainmentSaveVideonews_for_aajtk(title=title, videoPublicId=nameofvideo, videoUrl=videourl)
        obj.save()

        print('save in db')
        return HttpResponse('done')
    else:
        print('video not saved')


