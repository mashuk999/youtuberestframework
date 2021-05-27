from rest_framework import serializers
from .models import *

from rest_framework.serializers import Serializer, FileField

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']



class Entertainmentserializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()


class SaveVideoserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaveVideo
        fields = '__all__'

    def create(self, validated_data):
        return SaveVideo.objects.create(**validated_data)


class Get_Savevideoserializer(serializers.ModelSerializer):
    class Meta:
        model = SaveVideo
        fields = ['nameofvideo']



