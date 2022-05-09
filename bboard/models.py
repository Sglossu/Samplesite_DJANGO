from django.db import models
from django.contrib.auth.models import User

class Bb (models.Model) :
    title = models.CharField(max_length=50, verbose_name='Товар') # строковое поле фиксированной длины
    content = models.TextField(null=True, blank=True, verbose_name='Описание') # текстовое поле неограниченной длины, memo-поле, null и blank True значит можо не заполнять
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано') # auto_now_add=True - занесение текущего времениb1
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика') # ForeignKey - поле внешнего ключа, в котором хранится ключ записи из первичной модели
                                                                            # 1-й парам: имя класса первичной модели
                                                                            # on_delete управляет каскадными удалениями записей вторич модели после удаления записи первичной модели. PROTECT запрещает каскадные удаления
    
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
        constraints = (
            models.CheckConstraint(check=models.Q(price__gte=0) & \
                    models.Q(price__lte=1000000), name='bboard_rubric_price_constraints'),
        )
        
class Rubric (models.Model) :
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
        
class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Spare(models.Model):
    name = models.CharField(max_length=30)
    
class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)