from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse("App home. Hello!")

# Create your views here.
