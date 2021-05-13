from django.urls import path
from . import views

urlpatterns = [
    path("", views.travel_index, name="travel_index"),
    path("add/", views.travel_detail, name="travel_detail"),
]