from django.db import models
from django.utils import timezone

# Create your models here.


class Car(models.Model):
    znamka = models.TextField(max_length=128)
    model = models.TextField(max_length=128)
    ime = models.TextField(max_length=128)



class Comment(models.Model):
    car = models.ForeignKey(Car)
    body = models.TextField(timezone.now)
