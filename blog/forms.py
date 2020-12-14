"""here a form is beeing created for the user to make comments on the blogposts
the form is quite similar to a model but there is no argument"""
from django import forms
from .models import blog

class comment(forms.ModelForm):
    Comment = forms.CharField(max_length=250,
                              label="Ihr Kommentar",
                              widget=forms.TextInput(attrs={'style': 'width:800px', 'placeholder':'max. 250 Zeichen'})) #widget as a HTML representation of Input Field



    class Meta:
        model=blog
        fields=['Comment']



"""class blogentry(forms.Form):
    Comment=forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'Sie können Ihren Kommentar hier hinterlassen',
            'rows':10,
            'cols':70,
        }
        ))
"""
"""I still need to adjust the attributes, because for some reason it does not adjust the textfield to 10 and 70"""