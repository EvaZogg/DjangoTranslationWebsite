from django.contrib.auth.models import User
from django.db import models

# Defines indirectly the table "Contact" with the columns "desc, TranslationText, user, .." of the datatypes "CharField, TextField."
# python manage.py makemigrations and python manage.py migrate creates the table in the database system
class Contact(models.Model):
  desc = models.TextField()
  translationText = models.TextField(null=True)
  date = models.DateField()
  # file = models.FileField(null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) # Represents relationship to logged in User

