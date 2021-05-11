from django.shortcuts import render, redirect,  get_object_or_404
from .forms import UrlForm
from .models import Url
from django.contrib import messages


def index(req):
    if(req.method == "POST"):
        form = UrlForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data["long_url"])
            url, created = Url.objects.get_or_create(long_url = form.cleaned_data["long_url"])
            print(url.short_url, created)
            path = req.build_absolute_uri() 
            full_short_url = path + url.short_url
            messages.success(req, full_short_url)
            return redirect('/')

    else:
        form = UrlForm()
    
    return render(req, 'urls/index.html', {'form': form })



def redirect_user(req, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    long_url = url.long_url
    print(long_url)
    return redirect(long_url)

