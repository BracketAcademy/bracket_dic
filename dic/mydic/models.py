# Import things
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta

# Create your models here.


class word(models.Model):
    word_text = models.CharField(
        max_length=50, verbose_name="Word", null=False, blank=False)
    word_type = models.CharField(
        max_length=50, verbose_name="Type", null=False, blank=False)

    word_trans = models.CharField(
        max_length=200, verbose_name="Translation", null=False, blank=False)
    word_date = models.DateTimeField("Date Added")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def recent(self):
        return timezone.now() - timedelta(days=1) <= self.word_date <= timezone.now()
    recent.admin_order_field = 'word_date'
    recent.boolean = True
    recent.short_description = 'Published Recently?'

    def __str__(self):
        return self.word_text

    def deltadate(self):
        real_delta = timezone.now() - self.word_date
        if real_delta.days:
            return f'{real_delta.days}روز پیش'
        elif real_delta.seconds//3600 >= 1:
            return f'{real_delta.seconds//3600}ساعت پیش'
        elif real_delta.seconds//60 >= 1:
            return f'{real_delta.seconds//60}دقیقه پیش'
        elif real_delta.seconds:
            return f'{real_delta.seconds}ثانیه پیش'
        else:
            return 'همین الان!'
