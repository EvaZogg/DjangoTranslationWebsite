from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, UserForm
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # Form data is submitted in a POST request. Form data is processed.
        form = SignUpForm(request.POST) # Filled out form is generated.
        if form.is_valid(): # Validation of form data, e.g. "Password1" and "Password2" are equal, long enough, etc.
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # Try to enter new user. Check if username is still free.
            login(request, user) # Log in user after successful registration.
            return redirect('home') # Home page is shown.
    else:
        form = SignUpForm()
        # print (form)
    return render(request, 'accounts/signup.html', {'form': form})

# Contains all functionality to show and update a user in a form-based template (updateUser.html).
# The class "UpdateUserView" extends django built-in generic class "UpdateView"
# and defines its specific fields ("model", "form_class", "..") and methods ("test_func").
class UpdateUserView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = '/'
    template_name = "accounts/updateUser.html"

    # Method of class "UserPassesTestMixin" defaults to true.
    # We overwrite it and test if logged in user id is equal to primary key in url.
    def test_func(self):
        return self.kwargs['pk'] == self.request.user.id
