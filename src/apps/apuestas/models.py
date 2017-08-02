# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length = 200)
    due_date = models.DateTimeField('Fecha Limite')
    create_date = models.DateTimeField('fecha publicacion', auto_now_add = True)
    create_user = models.ForeignKey(User, related_name = "pregunta_create_user")
    update_date = models.DateTimeField('fecha publicacion', auto_now_add = True)
    update_user = models.ForeignKey(User, related_name = "pregunta_update_user")

    def __unicode__(self):
        return "%s" % (self.text)
    @property
    def respuestas(self):
        return RespuestasValidas.objects.filter(pregunta=self)

class RespuestasValidas(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField('fecha publicacion', auto_now_add = True)
    create_user = models.ForeignKey(User, related_name = "respuesta_create_user")
    update_date = models.DateTimeField('fecha publicacion', auto_now_add = True)
    update_user = models.ForeignKey(User, related_name = "respuesta_update_user")

    class Meta:
        unique_together = ('pregunta', 'text')

    def __unicode__(self):
        return "%s" % (self.text)
