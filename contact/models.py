from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  desc = models.TextField()
  translationText = models.TextField()
  date = models.DateField()

  def _str_(self):
    return self.name
