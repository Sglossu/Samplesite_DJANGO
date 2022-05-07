from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
    #  get_template -  загружаем шаблон, возвращает экземпляр класса Template
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    # формируем контекст шаблона - набор данных, которые будут выведены на генерируемой странице. Это словарь, переменные одноименные
    context = {'bbs' : bbs}
    # рендеринг шаблона, т.е. генерирование вебстраницы. request - экземпляр класса HttpRequest - клиентские запрос, полученный котроллером-функцией
    # результат - строку с HTML кодом передаем конструктуру класса HttpResponse для формирования ответа
    return HttpResponse(template.render(context, request))