from django.db import models
from django.contrib.auth.models import User

Fillieres = [
    ("1", "Chomage"),
    ("2", "BTS"),
    ("3", "DUT"),
    ("4", "Master"),
    ("5", "Licence"),
    ("6", "Doctorat"),
]


class Ecole(models.Model):
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    numeroDepartement = models.IntegerField()
    telephone = models.CharField(max_length=255)


class Offre(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    nombre_place = models.IntegerField()
    filliere = models.CharField(max_length=100, choices=Fillieres, default="1")
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)


class Demande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
