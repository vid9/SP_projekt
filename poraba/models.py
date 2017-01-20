from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.


class Znamka(models.Model):
    znamka = models.TextField(max_length=128)

class Car(models.Model):
    znamka = models.ForeignKey(Znamka, blank=True, null=True)
    model = models.TextField(max_length=128)
    #    imgfile =  models.ImageField(upload_to='images/%m/%d')

    def is_znamka(self):
        if self.znamka != 0:
            return True
        return False

class Specifikacije(models.Model):
    visina = models.IntegerField(default=0)
    dolzina = models.IntegerField(default=0)
    tip = models.BooleanField(default=0)
    vtanka = models.IntegerField(default=0)
    poraba = models.DecimalField(decimal_places=2, max_digits=4)
    ime = models.ForeignKey(Car, null=True)

    def min_poraba(self):
        if self.poraba < 8:
            return True
        return False

    class Meta:
        permissions = (
            ('add_car', 'Can add Car'),
        )

class CommentCar(models.Model):
    car = models.ForeignKey(Car)
    body = models.TextField(timezone.now)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def is_recent(self):
        """Returns True, if the article is recent (i.e. recent than 3 days)"""
        if self.pub_date + timedelta(days=3) >= timezone.now():
            return True

        return False

class CommentUser(models.Model):
    car = models.ForeignKey(Car)
    body = models.TextField(timezone.now)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def is_recent(self):
        """Returns True, if the article is recent (i.e. recent than 3 days)"""
        if self.pub_date + timedelta(days=3) >= timezone.now():
            return True

        return False

class UserCar(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    ime = models.ForeignKey(Car, null=True)
    poraba = models.DecimalField(decimal_places=2, max_digits=4)