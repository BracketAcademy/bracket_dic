from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(req):
    w = word.objects.order_by('word_text')
    return render(req, 'mydic/index.html', context={'word':w})

def detail(req, w_id):
    w = get_object_or_404(word, id=w_id)
    return render(req, 'mydic/detail.html', {'w':w})

def form(req):
    return render(req, 'mydic/form.html')

def submit(req):
    try:
        nw = req.POST['nword']
        ntype = req.POST['ntype']
        ntrans = req.POST['ntrans']
    except MultiValueDictKeyError:
        nw = req.GET['nword']
        ntype = req.GET['ntype']
        ntrans = req.GET['ntrans']
    ndate = timezone.now()

    w = word(word_text=nw, word_type=ntype, word_trans=ntrans, word_date=ndate)
    w.save()

    return HttpResponseRedirect(reverse('mydic:index'))