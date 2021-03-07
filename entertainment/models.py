from django.db import models

# Create your models here.


class Entertainmentdb(models.Model):
    title=models.CharField(max_length=500)
    nextrandom=models.DateTimeField()


class SaveVideo(models.Model):
    title=models.CharField(max_length=500)
    video=models.FileField(upload_to='',max_length=800)
    # slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("post_detail", kwargs={"slug": str(self.slug)})
