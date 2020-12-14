from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from datetime import datetime
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

# The URL <hostname:8000>/contact/ calls this function.
# This function displays the empty contact form using the template "contact/index.html".
# The user must be logged in. If not, the login form is displayed before.
@login_required
def index(request):
  return render(request, 'contact/index.html')

# After pressing the submit button the filled out form data will be
# sent to the server with the URL <hostname:8000>/contact/create as a post request.
@login_required
def create(request):
  if (request.method == 'POST'): # always true, could be omitted
    # Extract each filled out data item from request and assign it to variables "desc, translationText".
    desc = request.POST.get('description')
    translationText = request.POST.get('translationText')
    if (request.FILES['myfile']): # Request contains a file
      myfile = request.FILES['myfile'] # Extract submitted file from request
      fs = FileSystemStorage() # Open FileSystem
      filename = fs.save(myfile.name, myfile) # Save file in FileSystem
      contact = Contact(file=myfile, desc=desc, translationText=translationText, date=datetime.today(), user=request.user)
      contact.save()
    else:
      # Creates an object/instance of class Contact and assigns it to the variable "contact".
      # "user=request.user" assigns logged in User (request.user) to field "user" in model "Contact"
      contact = Contact(desc=desc, translationText=translationText, date=datetime.today(), user=request.user)
      # Method call "save" stores the data persistently in database table "Contact".
      contact.save()
    # Finally a conformation page will be displayed.
    return render(request, 'contact/confirm.html')