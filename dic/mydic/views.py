# Import things!
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .models import word

# Create your views here.


def index(req):
    w = word.objects.order_by('word_text')
    return render(req, 'mydic/index.html', context={'word': w})


def detail(req, w_id):
    w = get_object_or_404(word, id=w_id)
    return render(req, 'mydic/detail.html', {'w': w})


def form(req, wordex=''):
    return render(req, 'mydic/form.html', {'wordex': wordex})


@require_POST
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
                    return render(req, 'mydic/form.html', {'wordex': 'the word is registered!'})
                else:

                    return render(req, 'mydic/form.html', {'wordex': 'merge trans'})
            else:
                # merge tpye
                return render(req, 'mydic/form.html', {'wordex': 'merge type'})
        else:
            continue

    w.save()
    return redirect('mydic:index')


@require_POST
def search(req):
    try:
        searchtxt = req.POST['searchtxt']
    except MultiValueDictKeyError:
        searchtxt = req.GET['searchtxt']

    return render(req, 'mydic/search.html', context={'searchtxt': searchtxt})


def signup(req):
    if req.method=='GET':
        return render(req, 'mydic/signup.html')
    else:
        if 'susername' in req.POST:
            try:
                if req.POST['spassword1']==req.POST['spassword2']:
                    newuser = User.objects.create_user(username=req.POST['susername'], password=req.POST['spassword1'])
                    newuser.email = req.POST['semail']
                    newuser.save()
                    login(req, newuser)
                    return redirect('mydic:index')
                else:
                    return render(req, 'mydic/signup.html', context={'wordex': 'duplicate password'})
            except IntegrityError:
                return render(req, 'mydic/signup.html', context={'wordex': 'username already exist'})
        else:
            user = authenticate(req, username=req.POST['lusername'], password=req.POST['lpassword1'])
            if user is None:
                return render(req, 'mydic/signup.html', context={'wordex': 'username or password is wrong!'})
            else:
                login(req, user)
                return redirect('mydic:index')


@require_POST
def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('mydic:index')
