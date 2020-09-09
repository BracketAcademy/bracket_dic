from django.shortcuts import render
from .models import *

# Create your views here.

def index(req):
    w = word.objects.all()
    return render(req, 'mydic/index.html', context={'word':w})
def detail(req, w_id):
    w = word.objects.get(id=w_id)
    return render(req, 'mydic/detail.html', {'w':w})