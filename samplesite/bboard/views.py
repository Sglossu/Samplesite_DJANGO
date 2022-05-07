from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb

# index - контрОллер
def index(request):
    bbs = Bb.objects.all()
    # возвращает рендер готовго шаблона с помощью функции render из модуля shortcut
    return render(request, 'bboard/index.html', {'bbs' : bbs})