from django.db import models

# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=400)
    age=models.IntegerField()
    collage=models.TextField()
    placed=models.CharField(max_length=500)
    