from django.db import models

# Defines indirectly the table "Contact" with the columns "name, email, .." of the datatypes "CharField, TextField."
# python manage.py makemigrations and python manage.py migrate creates the table in the database system
class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  desc = models.TextField()
  translationText = models.TextField()
  date = models.DateField()

