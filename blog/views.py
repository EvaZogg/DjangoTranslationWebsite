from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .models import blog #benötigtes Model importieren
from .forms import blogentry

from django.http import HttpResponseRedirect
from django.shortcuts import render


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


"""def createblogentry(request):
    obj = blog.objects.get(id=1) #which specific object shall be opened
    my_form = blogentry(httprequest.POST or None, instance=obj) #opens the instance of the object

    if my_form.is_valid():
        my_form.save()
        my_form=blogentry()

    context = {
        "form" : my_form
    }
    return render(httprequest, "createblogentry_view.html", context)"""

def createblogentry(request):
    x=1
    obj = blog.objects.get(id=x)
    my_form = blogentry(request.POST or None, instance=obj)
    if my_form.is_valid():
        my_form.save()
        my_form=blogentry()

    context = {
        "form" : my_form
    }
    return render(request, "createblogentry_view.html", context)

