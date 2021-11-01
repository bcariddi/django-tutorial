from django.db import models

# Create your models here.
class Bug(models.Model):
    package = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    summary = models.TextField()

class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    content = models.TextField()