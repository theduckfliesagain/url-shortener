from django.shortcuts import render
from .forms import UrlForm
from .models import Url

def index(req):
    if(req.method == "POST"):
        form = UrlForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data["long_url"])
            url, created = Url.objects.get_or_create(long_url = form.cleaned_data["long_url"])
            print(url, created)

    else:
        form = UrlForm()
    
    return render(req, 'urls/index.html', {'form': form })

