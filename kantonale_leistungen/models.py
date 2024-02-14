from django.db import models


# Create your models here.

class Gemeinde(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Leistungsanbietende(models.Model):
    name = models.CharField(max_length=100)
    taetigkeit = models.TextField(blank=True)
    beschreibung = models.TextField(blank=True)
    leistung = models.BooleanField(default=False)
    gemeinde = models.ManyToManyField(Gemeinde, related_name='leistungsanbietende')
    internetlink = models.URLField(max_length=200, blank=True)  # Feld für den Internetlink

    def __str__(self):
        return self.name
