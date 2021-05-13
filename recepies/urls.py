from django.urls import path
from . import views

urlpatterns = [
    path("", views.recepies_list, name="recepies_list"),
    path("<category>/", views.recepies_category, name="recepies_category"),
]