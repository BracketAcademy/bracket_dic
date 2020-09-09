from django.shortcuts import render
from .models import *

# Create your views here.

def index(req):

    return render(req, 'mydic/index.html',)