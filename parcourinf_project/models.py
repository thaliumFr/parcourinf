from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404

Fillieres = [
    ("1", "Chomage"),
    ("2", "BTS"),
    ("3", "DUT"),
    ("4", "Master"),
    ("5", "Licence"),
    ("6", "Doctorat"),
]

Statuts = [
    ("1", "En attente"),
    ("2", "Acceptée"),
    ("3", "Refusée"),
]


class Ecole(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    numeroDepartement = models.IntegerField()
    telephone = models.CharField(max_length=255)
    img = models.CharField(
        default="https://st.depositphotos.com/1001911/4773/v/450/depositphotos_47738095-stock-illustration-begging-emoticon.jpg",
        max_length=255,
    )

    def offres(self):
        return Offre.objects.filter(ecole=self)

    def __str__(self):
        return self.nom


class Offre(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    nombre_place = models.IntegerField()
    filliere = models.CharField(max_length=100, choices=Fillieres, default="1")
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)


class Demande(models.Model):
    # Un utilisateur (compte) peut postuler à une offre
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Une demande est liée à une offre spécifique
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)

    # Statut de la demande
    statuts = models.CharField(max_length=100, choices=Statuts, default="1")

    def Accepte(self):
        self.statuts = "2"
        self.save()

    def Refuse(self):
        self.statuts = "3"
        self.save()

    def Postule(self):
        if Demande.objects.filter(user=self.user, offre=self.offre).exists():
            print(
                f"{self.user.get_full_name()} a déjà postulé à l'offre {self.offre.nom}"
            )
        else:
            nouvelle_demande = Demande(
                user=self.user, offre=self.offre
            )  # Création d'une nouvelle demande
            nouvelle_demande.save()  # Enregistrement de la demande
            print(
                f"La demande de {self.user.get_full_name()} pour l'offre {self.offre.nom} a été enregistrée"
            )


class Utilisateur(User):
    demande = models.ManyToManyField(Demande)
