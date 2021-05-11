from django import forms
from .models import Url
from django.forms.widgets import TextInput


class UrlForm(forms.ModelForm):

    long_url = forms.URLField(max_length=200, 
                     help_text="Please enter the URL of the page.", 
                     initial="http://",
                     widget=TextInput)

    class Meta:
        model = Url
        fields= ['long_url']
