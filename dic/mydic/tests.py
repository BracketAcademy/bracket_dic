from django.test import TestCase
from mydic.models import word
from django.utils import timezone
from datetime import timedelta


# Create your tests here.
class wordModelTest(TestCase):
    def test_recent_future(self):
        time = timezone.now() + timedelta(seconds=1)
        objtest = word(word_date=time)
        self.assertIs(objtest.recent(), True)