import datetime
from django.db import models
from django.forms import ValidationError

# Create your models here.

class Convocatoria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)
    date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return self.title
    

class Teams(models.Model):
    nonmbre_equipo = models.CharField(max_length=100)
    captain_id = models.IntegerField()
    participant1 = models.CharField(max_length=300)
    participant2 = models.CharField(max_length=300)
    participant3 = models.CharField(max_length=300)
    participant4 = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.nonmbre_equipo} en {self.Convocatoria}"
    
    def clean(self):
        if self.integrantes != 4:
            raise ValidationError("El equipo debe tener 4 integrantes")
        super().clean()

