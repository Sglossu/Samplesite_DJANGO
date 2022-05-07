from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb, Rubric

# index - контрОллер
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs' : bbs, 'rubrics' : rubrics}
    # возвращает рендер готовго шаблона с помощью функции render из модуля shortcut
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id): # rubric_id будет присвоено значение URL параметра, выбранное из интернет-адреса
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs' : bbs, 'rubrics' : rubrics, 'curent_rubric' : current_rubric}
    return render(request, 'bboard/by_rubric.html', context)