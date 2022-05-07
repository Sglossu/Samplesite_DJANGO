from django.contrib import admin

from .models import Bb

# добавление класса-редактора
class BbAdmin(admin.ModelAdmin) :
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

# admin.site - экземпляр класса AdminSite (представляет административный сайт), хранится в переменной site
admin.site.register(Bb, BbAdmin)
