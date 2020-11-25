from django.shortcuts import render
from datetime import datetime
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required

def index(request):
  return render(request, 'contact/index.html')

@login_required
def create(request):
  if (request.method == 'POST'):
    name = request.POST.get('name')
    email = request.POST.get('email')
    desc = request.POST.get('description')
    translationText = request.POST.get('translationText')
    contact = Contact(name=name, email=email, desc=desc, translationText=translationText, date=datetime.today())
    contact.save()
  return render(request, 'contact/confirm.html')