from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .models import blog  # benötigtes Model importieren
from .forms import blogentry
from django import template

register = template.Library()

from django.http import HttpResponseRedirect
from django.shortcuts import render


# The following was just a test
# def blog_view(httprequest, *args):
# test_dict = {
# "name" : "max",
# "testlist" : ["this", "is", "a", "test", "blogpost"],
# }
# return render(httprequest, 'blog.html', test_dict)

# Create your views here.
def blog_view(httprequest, *args, **kwargs):  # create function called blog_view/ args beacuse of variable Nr. auf Parameters passed/ **kwargs because of unknown amount of keyword Arguments
    blogdata = blog.objects.all()  # Saves objects from DB in Variable blogdata which is called in Template

    context = {
        "blogdata": blogdata,  # Dictionary beeing created with the name blogdata
        "Title": "Blogposts related to technical Translation",
        'form': blogentry()

    }

    if httprequest.method == "POST":
        createblogentry(httprequest) #if so. write we open createblogentry, rename!!
        #return render(httprequest, "blog.html", context)


    return render(httprequest, "blog.html", context)


def createblogentry(request):

    title = request.POST["title"]
    #date = request.POST["date"]
    obj = blog.objects.get(title=title) #which specific object shall be opened
    my_form = blogentry(request.POST, instance=obj)
    #print(my_form)#opens the instance of the object

    if my_form.is_valid():
        my_form.save()
        my_form = blogentry()

    else:
        my_form = blogentry()
    context = {
        "form" : my_form,
    }
    return render(request, "blog.html", context)

"""@register.inclusion_tag("blog.html")
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
    #return render(request, "createblogentry_view.html", context)
    return {"hallo":x}"""
