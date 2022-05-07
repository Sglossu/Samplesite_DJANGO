from django.db import models

class Bb (models.Model) :
    title = models.CharField(max_length=50) # строковое поле фиксированной длины
    content = models.TextField(null=True, blank=True) # текстовое поле неограниченной длины, memo-поле, null и blank True значит можо не заполнять
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True) # auto_now_add=True - занесение текущего времениb1
