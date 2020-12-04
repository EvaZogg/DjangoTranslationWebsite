from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .models import blog #benötigtes Model importieren
from .forms import blogentry
#The following was just a test
#def blog_view(httprequest, *args):
    #test_dict = {
        #"name" : "max",
        #"testlist" : ["this", "is", "a", "test", "blogpost"],
    #}
    #return render(httprequest, 'blog.html', test_dict)

# Create your views here.
def blog_view(httprequest, *args, **kwargs): #create function called blog_view/ Argument hhtprequest so there will be an httepresponse
    blogdata = blog.objects.all() #returns all Objects which have been defined as a list
    context = {
        "blogdata":blogdata, #List der Objekte wird weitergegeben
        "Title":"Blogposts related to technical Translation"
    }
    return render(httprequest, "blog.html", context)

def blog_view2(httprequest, *args, **kwargs):
    oneblog = blog.objects.get(id=1)
    context = {
        "obj":oneblog,
        "Title":"Latest Blogpost"
    }
    return render(httprequest, "blog_view2.html", context)

def createblogentry(httprequest, *args, **kwargs):
    my_form = blogentry() #link to the form, which was imported before
    context = {
        "my_form" : my_form
    }
    return render(httprequest,
                  "createblogentry_view.html.html", context)