"""here a form is beeing created for the user to make comments on the blogposts
The commen shall be less or 250 characters, in the blox it will show that the input is restricted to 250 characters."""
from django import forms
from .models import blog

class comment(forms.ModelForm):
    Comment = forms.CharField(max_length=250,
                              label="your comment",
                              widget=forms.TextInput(attrs={'style': 'width:800px', 'placeholder':'max. 250 characters'})) #widget as a HTML representation of Input Field



    class Meta: #further options
        model=blog
        fields=['Comment']



