from django.db import models

# Create your models here.
class word(models.Model):
    word_text = models.CharField(max_length=50)
    word_type = models.CharField(max_length=50)

    word_trans = models.CharField(max_length=200)