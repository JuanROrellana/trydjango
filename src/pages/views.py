from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("Hello World1")
