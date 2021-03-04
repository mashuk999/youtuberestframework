from django.db import models

# Create your models here.


class Entertainmentdb(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateTimeField()