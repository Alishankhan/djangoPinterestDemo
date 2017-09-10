from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tags(models.Model):
    description = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField('date published')

class Post(models.Model):

    title = models.CharField(max_length=100,null=False)
    slug = models.CharField(max_length=500,null=False)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    dateCreated = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tags)
    user = models.ForeignKey(User)
