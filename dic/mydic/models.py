from django.db import models
from datetime import datetime as D
# Create your models here.
class word(models.Model):
    word_text = models.CharField(max_length=50)
    word_type = models.CharField(max_length=50)

    word_trans = models.CharField(max_length=200)
    word_date = models.DateTimeField("date added")
    def recent(self):
        b=D.now()
        a=self.word_date
        c=a-b
        if c.days<1:
            h=c.seconds//3600
            if h<=12:
                True
            else:
                False
        else:
            False
        del a,b,c,h

