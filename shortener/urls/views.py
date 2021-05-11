from django.shortcuts import render
from .forms import UrlForm

def index(req):
    
    return render(req, 'urls/index.html', {'form': UrlForm() })
