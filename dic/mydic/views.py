from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(req):
    w = word.objects.order_by('word_text')
    return render(req, 'mydic/index.html', context={'word':w})

def detail(req, w_id):
    w = get_object_or_404(word, id=w_id)
    return render(req, 'mydic/detail.html', {'w':w})