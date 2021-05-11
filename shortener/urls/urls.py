from django.urls import path
from . import views

# app_name = "urls"
urlpatterns = [
    path("", views.index, name="urls-index")
]

