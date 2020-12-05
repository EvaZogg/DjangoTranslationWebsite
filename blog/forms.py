"""here a form is beeing created for the user to make comments on the blogposts
the form is quite similar to a model but there is no argument"""
from django import forms

class blogentry(forms.Form):
    Comment=forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'Sie können Ihren Kommentar hier hinterlassen',
            'rows':10,
            'cols':70,
        }
        ))
"""I still need to adjust the attributes, because for some reason it does not adjust the textfield to 10 and 70"""