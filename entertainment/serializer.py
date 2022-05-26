from rest_framework import serializers
from .models import *
from rest_framework.serializers import Serializer, FileField


class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']



class Entertainmentserializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()


class Newsserializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()

class Newsserializer_for_aajtk(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()

class Technologyserializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()


class SaveVideoserializer(serializers.ModelSerializer):
    class Meta:
        model = SaveVideo_entertainment
        fields = '__all__'

    def create(self, validated_data):
        return SaveVideo_entertainment.objects.create(**validated_data)


class Get_Savevideoserializer(serializers.ModelSerializer):
    class Meta:
        model = SaveVideo_entertainment
        fields = ['nameofvideo']



