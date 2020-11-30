from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
def blog_view(httprequest, *args):
    test_dict = {
        "name" : "max",
        "testlist" : ["this", "is", "a", "test", "blogpost"],
    }
    return render(httprequest, 'blog.html', test_dict)