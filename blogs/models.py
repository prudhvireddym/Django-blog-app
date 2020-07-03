from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    image = models.FilePathField(path="/img")
