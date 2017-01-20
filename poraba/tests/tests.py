from django.test import TestCase
import datetime

from django.utils import timezone

from poraba.models import User, Car, Znamka, Specifikacije, CommentUser


# Create your tests here.


class CommentUserTests(TestCase):
    def test_is_recent(self):
        """
        is_recent() should return True, if the publish date is recent; False
        otherwise.

           car = models.ForeignKey(Car)
    body = models.TextField(timezone.now)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        """
        a = CommentUser(car=Car(model="model", znamka=Znamka(znamka="Audi")), body='', pub_date=timezone.now(), author=User())
        b = CommentUser(car=Car(model="model", znamka=Znamka(znamka="Audi")), body='', pub_date=timezone.now()-datetime.timedelta(days=30), author=User())

        self.assertIs(a.is_recent(), True)
        self.assertIs(b.is_recent(), False)

class SpecifikacijeTests(TestCase):
    def test_min_poraba(self):
        """
        is_recent() should return True, if the publish date is recent; False
        otherwise.
        """

        min = Specifikacije(visina=1000, dolzina=1000, tip=True, vtanka=40, poraba =7, ime=Car(model="model", znamka=Znamka(znamka="Audi")))
        max = Specifikacije(visina=1000, dolzina=1000, tip=True, vtanka=40, poraba=9, ime=Car(model="model", znamka=Znamka(znamka="Audi")))

        self.assertIs(min.min_poraba(), True)
        self.assertIs(max.min_poraba(), False)

class CarTests(TestCase):
    def test_is_znamka(self):
        a = Car(model="model", znamka=Znamka(znamka="Audi"))
        b = Car(model="model", znamka=Znamka(znamka="BMW"))

        self.assertIs(a.is_znamka(), True)
        self.assertIs(b.is_znamka(), True)