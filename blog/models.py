from django.db import models
from django.views.generic import View   #wird für view die auf Klasses beruhen benötigt
import datetime


# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    Blogtext=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    Comment=models.TextField(max_length=1000)
