from django.db import models

class Rimed(models.Model):
    scientific_name = models.CharField(max_length=255)
    vernacular_names = models.CharField(max_length=255)
    botanical_family = models.CharField(max_length=255)
    dosage = models.TextField()
    description = models.TextField()
    parts_used = models.CharField(max_length=255)
    toxicity_rating = models.IntegerField()
    efficacy_rating = models.IntegerField()
    countries_found = models.CharField(max_length=255)
    not_for_children = models.BooleanField()
    not_for_elderly = models.BooleanField()
    not_for_pregnant_women = models.BooleanField()
    INFLAMMATION_GANGLIONNAIRE = models.BooleanField()
    HEPATOPATHIES = models.BooleanField()
    NAUSEES = models.BooleanField()
    HYGIENE_APRES_ACCOUCHEMENT = models.BooleanField()
    PRURIT = models.BooleanField()
    RHUMATISMES = models.BooleanField()
    CHOC_EMOTIONNEL = models.BooleanField()
    RHUME = models.BooleanField()
    ANTISPASMODIQUE = models.BooleanField()
    MAUX_DE_DENTS_ET_DOREILLE = models.BooleanField()
    FLATULENCES = models.BooleanField()
    CANDIDOSE_BUCCALE = models.BooleanField()
    ASTHME = models.BooleanField()
    ASTHENIE = models.BooleanField()
    CONSTIPATION = models.BooleanField()
    PARASITOSES_INTESTINALES = models.BooleanField()
    ANEMIE = models.BooleanField()
    CEPHALEE = models.BooleanField()
    BRULURES = models.BooleanField()
    BLESSURES = models.BooleanField()
    PNEUMOPATHIES = models.BooleanField()
    DYSPEE = models.BooleanField()
    ACTIVITES_PHANNACOLOGIQUES = models.BooleanField()
    PEDICULOSE = models.BooleanField()
    AMENORRHEE = models.BooleanField()
    VERRIGES = models.BooleanField()
    VOMISSEMENTS = models.BooleanField()
    ENTORSES_TRAUMATISMES = models.BooleanField()
    FIEVRE = models.BooleanField()
    DIAHREES = models.BooleanField()

    def __str__(self):
        return self.vernacular_names