# coding=utf-8
from django.shortcuts import render
from .models import *
from django.db.models import F
def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    print("hongbiao------------", len(list))
    conttext = {"list": list}
    return render(request, 'ObjectMoudel/index.html', conttext)
