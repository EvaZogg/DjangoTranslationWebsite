"""DjangoTranslationWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from blog.views import blog_view, createcomment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Uses the provided URLconf in "django.contrib.auth.urls".
    # Defines paths for "accounts/login/, accounts/logout/, accounts/password_change/, ..".
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', blog_view),
    path('comment/', createcomment),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#in order to include the staic pictures by using the pillow framework