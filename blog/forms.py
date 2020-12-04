"""here a form is beeing created for the user to make comments on the blogposts
the form is quite similar to a model but there is no argument"""
from django import forms

class blogentry(forms.Form):
    Comment=forms.CharField(
        required=False,
        label='new label',
        widget=forms.Textarea(attrs={
        'class' : 'my-new-cass',
        'id' : 'my-id-field',
        'placeholder' : 'Please enter your comment here. (reminder: comments shall respect the comment guidlines.)',
        'rows' : 20,
        'cols' : 70
    }
))
