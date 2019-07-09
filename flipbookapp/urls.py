from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:collection_id>/", views.collection_details,
         name="collection_details")
]
