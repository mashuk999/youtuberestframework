from django.db import models


class SaveVideo_entertainment(models.Model):
    title=models.CharField(max_length=500)
    nameofvideo=models.CharField(max_length=200)
    videoPublicId = models.CharField(max_length=1000)
    videoUrl = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
