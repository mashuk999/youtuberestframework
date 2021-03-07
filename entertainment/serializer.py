from rest_framework import serializers
from .models import *

class Entertainmentserializer(serializers.Serializer):
    title=serializers.CharField(max_length=500)
    nextrandom=serializers.DateTimeField()
