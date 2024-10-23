from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.twig")


def ecoles_list(request):
    ecoles = Ecole.objects.all()
    return render(request, "ecoles.twig", {"ecoles": ecoles})


def ecole(request, pk):
    ecole = get_object_or_404(Ecole, pk=pk)
    return render(request, "ecole.twig", {"ecole": ecole})


def offres_list(request):
    offres = Offre.objects.all()
    return render(request, "offres.twig", {"offres": offres})
