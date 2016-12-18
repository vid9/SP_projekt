from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Comment(models.Model):
  comment = models.TextField()
  color = models.CharField(max_length=10, null=True)
  pub_date = models.DateTimeField( default=datetime.now )
  article = models.ForeignKey( Avto, on_delete=models.CASCADE )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Avto(models.Model):
  znamka = models.TextField()
  serija = models.models.TextField()
  model = models.models.TextField()