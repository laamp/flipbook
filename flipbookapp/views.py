from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, User


def home(req):
    return HttpResponse("App home. Hello!")


def collection_details(req, collection_id):
    collection = Collection.objects.get(id=collection_id)
    context = {collection_id: {"id": collection_id, "title": collection.title}}
    # return render(req, "flipbookapp/index.html", context)
    return HttpResponse(f"Details for collection #{context}")

# Create your views here.
