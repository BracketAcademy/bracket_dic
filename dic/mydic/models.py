from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class word(models.Model):
    word_text = models.CharField(max_length=50, verbose_name="Word")
    word_type = models.CharField(max_length=50, verbose_name="Type")

    word_trans = models.CharField(max_length=200, verbose_name="Translation")
    word_date = models.DateTimeField("Date Added")

    def recent(self):
        return timezone.now() - timedelta(hours=12) <= self.word_date <= timezone.now()
        '''
        b=timezone.now()
        a=self.word_date
        c=b-a
        if c.days<1:
            h=c.seconds//3600
            if h<=12:
                return True
            else:
                return False
        else:
            return False
        del a,b,c,
        '''
        
    def __str__(self):
        return self.word_text
