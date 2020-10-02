from django.contrib import admin
from .models import *

# Register your models here.
class wordAdmin(admin.ModelAdmin):
    list_display = ('word_text', 'word_type', 'word_trans', 'recent')
    list_filter = ['word_date']
    search_fields = ['word_text', 'word_trans']

admin.site.register(word, wordAdmin)