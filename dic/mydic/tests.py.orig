from django.test import TestCase
from mydic.models import word
from django.utils import timezone
from datetime import timedelta


# Create your tests here.
class wordModelTest(TestCase):
    def test_recent_future(self):
        time = timezone.now() + timedelta(seconds=1)
        objtest = word(word_date=time)
        self.assertIs(objtest.recent(), False)

    def test_recent_ok(self):
        time = timezone.now() - timedelta(hours=11, minutes=59, seconds=59)
        objtest = word(word_date=time)
        self.assertIs(objtest.recent(), True)

    def test_recent_past(self):
        time = timezone.now() - timedelta(hours=12, minutes=0, seconds=1)
        objtest = word(word_date=time)
        self.assertIs(objtest.recent(), False)