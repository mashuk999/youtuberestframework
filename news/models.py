from django.db import models




class Entertainmentdb(models.Model):
    title=models.CharField(max_length=500)
    nextrandom=models.DateTimeField()


class SaveVideo_news(models.Model):
    title=models.CharField(max_length=500)
    videoPublicId = models.CharField(max_length=1000)
    videoUrl = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
