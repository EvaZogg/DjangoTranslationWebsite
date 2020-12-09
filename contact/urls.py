from django.urls import path

from contact import views

urlpatterns = [
  path('', views.index, name='index'),
  # <hostname:8000>/contact/create calls function "create" in "views.py"
  path('create', views.create, name='create'),
]