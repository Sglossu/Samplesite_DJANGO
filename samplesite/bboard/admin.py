from django.contrib import admin

from .models import Bb, Rubric

# добавление класса-редактора
class BbAdmin(admin.ModelAdmin) :
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

# admin.site - экземпляр класса AdminSite (представляет административный сайт), хранится в переменной site
admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
