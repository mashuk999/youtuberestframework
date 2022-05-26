from django.db import models

class entertainmentNewsdb(models.Model):
    title=models.CharField(max_length=500)
    nextrandom=models.DateTimeField()

    def __str__(self):
        return self.title

class entertainmentNewsdb_for_aajtk(models.Model):
    title=models.CharField(max_length=500)
    nextrandom=models.DateTimeField()

    def __str__(self):
        return self.title


class entertainmentSaveVideonews(models.Model):
    title=models.CharField(max_length=500)
    videoPublicId = models.CharField(max_length=1000)
    videoUrl = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class entertainmentSaveVideonews_for_aajtk(models.Model):
    title=models.CharField(max_length=500)
    videoPublicId = models.CharField(max_length=1000)
    videoUrl = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title