from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from entertainment.serializer import *
from . models import *
import datetime


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@api_view(('GET',))
def cleanupFunction(request):
    if request.method == 'GET':
        NextDay_Date = datetime.datetime.today() - datetime.timedelta(days=1)
        print(NextDay_Date)
        formatted = NextDay_Date.strftime("%y-%m-%d")
        print(formatted)
        topics = entertainmentSaveVideonews_for_aajtk.objects.filter(videoPublicId__icontains=formatted)
        print(topics)
        serializer = Get_Savevideoserializer_of_aajtk(topics, many=True)

        return Response(serializer.data)
