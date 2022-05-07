from django.urls import path

from .views import index, by_rubric, BbCreateView

urlpatterns = [
    # маршрутр, указвыающий на контроллер
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric),
    path('', index),
]