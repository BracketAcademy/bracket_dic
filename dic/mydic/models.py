from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class word(models.Model):
    word_text = models.CharField(max_length=50, verbose_name="Word",null=False,blank=False)
    word_type = models.CharField(max_length=50, verbose_name="Type",null=False,blank=False)

    word_trans = models.CharField(max_length=200, verbose_name="Translation",null=False,blank=False)
    word_date = models.DateTimeField("Date Added")

    def recent(self):
        return timezone.now() - timedelta(hours=12) <= self.word_date <= timezone.now()
        
    def __str__(self):
        return self.word_text
