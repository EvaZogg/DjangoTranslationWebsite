from .models import blog
from .forms import comment
from django import template

register = template.Library()

from django.shortcuts import render

# Create your views here.
"""function which acesses the Blogpost object from the Database passes it in the conext where a Title and the user 
Input from the form is added. If a user makes a Comment the createcomment function is called.
The context is rendert."""
def blog_view(httprequest, *args, **kwargs): #  create function
    blogdata = blog.objects.all()  # Saves objects from DB in Variable blogdata which is called in blog.html

    context = { #the conext dictionary is created
        "blogdata": blogdata,  # key:blogdata and value blogdata
        "Title": "Blogposts related to technical Translation", #key: Title and value Blogpost related...
        'form': comment() #key: form and value is the user comment
    }

    if httprequest.method == "POST": #user is creating a POST request
        createcomment(httprequest) #createcomment is called
    return render(httprequest, "blog.html", context) #and Page is rendert again so the comment gets shown

"""createcomment is beeing executed if the used decides to make a comment on a blogpost. The comment is assigned to 
the correct object by title. If user entry is valid, it is saved in the Database using the form. Otherwise the comment
will not be saved and the form will be shown again. In the End the Blog is rendet again the the user can see his 
comment"""
def createcomment(request): #TODO create a seperate data for Comment so comment doesnt get overwriten

    title = request.POST["title"]
    #date = request.POST["date"] #a second layer in case there would be two blogpost with the same title
    obj = blog.objects.get(title=title) #The comment is assigned to the correct object b its title
    my_form = comment(request.POST, instance=obj)

    if my_form.is_valid(): #validation
        my_form.save() #save comment with the correct object
        my_form = comment()

    else: #if previous conditions dont apply
        my_form = comment()
    context = { #context will show the form
        "form" : my_form,
    }
    return render(request, "blog.html", context) #context is rendered
