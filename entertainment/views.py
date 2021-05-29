from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from.models import *
from .serializer import SaveVideoserializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


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




# class VideoUpload(generics.CreateAPIView):
#     serializer_class = SaveVideoserializer
#     def post(self, request, format=None):
#         serializer = SaveVideoserializer(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# def downloadvideofromheroku(request):
#     try:
#         filepath = request.GET['urlpath']
#         print(filepath)
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#         print(MEDIA_ROOT)
#         print(os.path.join(MEDIA_ROOT, filepath))
#         response = HttpResponse()
#         response['Content-Type'] = 'video/mp4'
#         response['X-Accel-Redirect'] = os.path.join(MEDIA_ROOT,filepath)
#         response['Content-Disposition'] = 'attachment;filename=' + os.path.join(MEDIA_ROOT,filepath)
#     except Exception:
#         raise Http404
#     return response
#
#
#
# def downloadvideofromheroku2(request):
#     try:
#         filepath = request.GET['urlpath']
#         print(filepath)
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#         print(MEDIA_ROOT)
#         print(os.path.join(MEDIA_ROOT, filepath))
#         from wsgiref.util import FileWrapper
#         file = FileWrapper(open(os.path.join(MEDIA_ROOT,filepath), 'rb'))
#         response = HttpResponse(file, content_type='video/mp4')
#         response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
#         return response
#     except Exception:
#         raise Http404










