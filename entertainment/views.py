from pathlib import Path
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from entertainment import processArticle
from .models import *
import os
from .serializer import Entertainmentserializer,SaveVideoserializer
import datetime,random
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics




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


def test(request):
    currdate=datetime.datetime.now()
    b=datetime.timedelta(2)
    c=currdate-b
    print(c.date())
    for i in SaveVideo.objects.all():
        a=i.date.date()
        print(a)
        if a==currdate.date():
            print('good')
            i.delete()


    return HttpResponse('ok')





