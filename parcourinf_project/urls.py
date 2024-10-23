from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ecoles", views.ecoles_list, name="ecoles_list"),
    path("ecole/<int:pk>/", views.ecole, name="ecole"),
    path("offres", views.offres_list, name="offres_list"),
]
