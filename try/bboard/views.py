from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rubric
from .forms import BbForm

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

# высокоуровневый контроллер-класс
class BbCreateView(CreateView):
    # templeta_name - путь к файлу-шаблону, создающему страницу с формой
    template_name = 'bboard/create.html'
    # form_class - ссылка на класс формы, связанный с моделью
    form_class = BbForm
    # success_url - адрес для перенаправления после успешного сохранения данных
    success_url = reverse_lazy('index')
    
    # переопределяем метод get_context_data так как должен выводиться контекст рубрик
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавляем список рубрик
        context['rubrics'] = Rubric.objects.all()
        return context