from django.db import models

# Create your models here.


class Entertainmentdb(models.Model):
    title=models.CharField(max_length=500)
    nextrandom=models.DateTimeField()


class SaveVideo(models.Model):
    title=models.CharField(max_length=500)
    video=models.FileField(upload_to='tmp',max_length=800)