from django.db import models
from django.views.generic import View   #wird für view die auf Klasses beruhen benötigt

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    Blogtext=models.TextField()
    Date=models.DateField.auto_now_add=True
    Comment=models.TextField(max_length=1000)
