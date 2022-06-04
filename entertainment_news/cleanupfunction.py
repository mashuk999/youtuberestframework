from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from entertainment.serializer import *
from . models import *


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@api_view(('GET',))
def cleanupFunction(request):
    if request.method == 'GET':
        topics = entertainmentSaveVideonews_for_aajtk.objects.all()
        serializer = Get_Savevideoserializer_of_aajtk(topics, many=True)
        return Response(serializer.data)