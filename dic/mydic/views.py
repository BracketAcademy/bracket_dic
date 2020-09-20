from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(req):
    w = word.objects.order_by('word_text')
    return render(req, 'mydic/index.html', context={'word':w})

def detail(req, w_id):
    w = get_object_or_404(word, id=w_id)
    return render(req, 'mydic/detail.html', {'w':w})

def form(req, wordex=''):
    return render(req, 'mydic/form.html', {'wordex':wordex})

def submit(req):
    try:
        nw = req.POST['nword'].lower()
        ntype = req.POST['ntype'].lower()
        ntrans = req.POST['ntrans'].lower()
    except MultiValueDictKeyError:
        nw = req.GET['nword'].lower()
        ntype = req.GET['ntype'].lower()
        ntrans = req.GET['ntrans'].lower()
    ndate = timezone.now()

    w = word(word_text=nw, word_type=ntype, word_trans=ntrans, word_date=ndate)

    aword = list()
    for i in word.objects.all():
        aword.append({
            'text': i.word_text,
            'type': i.word_type,
            'trans': i.word_trans
        })
    for i in aword:
        if w.word_text == i['text']:
            if w.word_type == i['type']:
                if w.word_trans == i['trans']:
                    return render(req, 'mydic/form.html', {'wordex':'the word is registered!'})
                else:
                    
                    return render(req, 'mydic/form.html', {'wordex':'merge trans'})
            else:
                #merge tpye
                return render(req, 'mydic/form.html', {'wordex':'merge type'})
        else:
            continue
        
    w.save()
    return HttpResponseRedirect(reverse('mydic:index'))

def search(req):
    try:
        searchtxt = req.POST['searchtxt']
    except MultiValueDictKeyError:
        searchtxt = req.GET['searchtxt']

    return render(req, 'mydic/search.html', context={ 'searchtxt':searchtxt })

def signup(req):

    return render(req, 'mydic/signup.html')