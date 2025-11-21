from django.template import loader

from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bboard


def index(request):
    template = loader.get_template('index.html')
    bbs = Bboard.objects.all()
    context = {'bbs': bbs}


    return render(request, 'index.html', context)
