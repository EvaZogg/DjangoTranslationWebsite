from django.db import models
import datetime


# Create your models here.
"""the model for the Blogojects is created"""
class blog(models.Model):
    title=models.CharField(max_length=200)
    Blogtext=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    Comment=models.TextField(max_length=1000, blank=True)
    Image=models.ImageField(upload_to='static', blank=True)

