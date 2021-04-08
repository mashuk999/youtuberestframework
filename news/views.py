from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from entertainment import processArticle
from entertainment.models import *
from entertainment.serializer import Entertainmentserializer,SaveVideoserializer
import datetime,random




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




@csrf_exempt
def savevideourl(request):
    if request.method == 'POST':
        # file = request.data.get('video')
        title = request.POST.get('title')
        videopublicid = request.POST.get('videoPublicId')
        videourl = request.POST.get('videoUrl')
        obj = SaveVideo(title=title, videoPublicId=videopublicid, videoUrl=videourl)
        obj.save()

        print('save in db')
        return HttpResponse('done')



def test(request):
    return HttpResponse('well done mate')