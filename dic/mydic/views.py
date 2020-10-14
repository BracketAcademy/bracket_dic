# Import things!
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import QuerySet

from .models import word

# Create your views here.


@require_GET
def index(req):
    w = word.objects.order_by('-word_date')
    w = list(w)
    wil = list()
    for i in w:
        if i.recent():
            wil.append(i)
    del w
    return render(req, 'mydic/index.html', context={'word': wil})


@require_GET
def detail(req, w_id):
    w = get_object_or_404(word, id=w_id)
    return render(req, 'mydic/detail.html', {'w': w})


@require_GET
def form(req, wordex=''):
    if req.user.is_authenticated:
        return render(req, 'mydic/form.html', {'wordex': wordex})
    else:
        return redirect('mydic:signup')


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
                    return render(req, 'mydic/form.html', {'wordex': 'این کلمه قبلا اضافه شده‌است!'})
                else:
                    # TODO: merge translation
                    return render(req, 'mydic/form.html', {'wordex': 'این کلمه قبلا اضافه شده‌است!'})
            else:
                # TODO: merge tpye
                return render(req, 'mydic/form.html', {'wordex': 'این کلمه قبلا اضافه شده‌است!'})
        else:
            continue

    w.user = req.user
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
    if req.method == 'GET':
        return render(req, 'mydic/signup.html')
    else:
        if 'susername' in req.POST:
            try:
                if req.POST['spassword1'] == req.POST['spassword2']:
                    newuser = User.objects.create_user(
                        username=req.POST['susername'], password=req.POST['spassword1'])
                    newuser.first_name = req.POST['sfirstname']
                    newuser.last_name = req.POST['slastname']
                    newuser.save()
                    login(req, newuser)
                    return redirect('mydic:index')
                else:
                    return render(req, 'mydic/signup.html', context={'wordex': 'رمزهای عبور همخوانی ندارد!'})
            except IntegrityError:
                return render(req, 'mydic/signup.html', context={'wordex': 'فردی با این نام کاربری وجود دارد!'})
        else:
            user = authenticate(
                req, username=req.POST['lusername'], password=req.POST['lpassword1'])
            if user is None:
                return render(req, 'mydic/signup.html', context={'wordex': 'نام کاربری یا رمز عبور نادرست است!'})
            else:
                login(req, user)
                return redirect('mydic:index')


@require_POST
def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('mydic:index')


@require_GET
def aboutus(req):
    return render(req, 'mydic/about.html')
