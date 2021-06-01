from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from.models import *

@csrf_exempt
def savevideourl(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        videopublicid = request.POST.get('videoPublicId')
        videourl = request.POST.get('videoUrl')
        nameofvideo=request.POST.get('name')
        obj = SaveVideo_entertainment(title=title, videoPublicId=videopublicid, videoUrl=videourl,nameofvideo=nameofvideo)
        obj.save()

        print('save in db')
        return HttpResponse('done')














