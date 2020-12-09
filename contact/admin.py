from django.contrib import admin
from contact.models import Contact

# Register your models here.

# Registers model "Contact" in order to make it visible on admin page <hostname:8000>/admin/.
admin.site.register(Contact)