from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from entertainment.serializer import *


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@api_view(('GET',))
def cleanupfunction(request):
    if request.method == 'GET':
        topics = SaveVideo.objects.all()
        serializer = Get_Savevideoserializer(topics, many=True)
        return Response(serializer.data)