from django.urls import path
from accounts import views
from .views import UpdateUserView

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  # pk is the primary key of the user
  path('updateUser/<int:pk>/', UpdateUserView.as_view(), name='updateUser'),
]