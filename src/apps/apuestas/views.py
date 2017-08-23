# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse
from .forms import PreguntaForm, ApuestasForm
from .models import Pregunta


@login_required
def apuestas_list(request):
    template = loader.get_template('apuestas_list.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username': request.user.username,
        'pregunta_list': pregunta_list
    }
    return HttpResponse(template.render(context, request))


class PreguntaView(LoginRequiredMixin, View):
    form = PreguntaForm()
    template_name = "pregunta_form.html"

    def get(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(instance=prg)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(data=request.POST, instance=prg)
        if form.is_valid():
            prg = form.save(commit=False)
            prg.save()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@login_required
def apuesta(request, id_pregunta):
    template = loader.get_template('apuesta.html')
    pregunta = Pregunta.objects.get(pk=id_pregunta)
    form = ApuestasForm(pregunta, request.user)
    if request.method == 'POST':
        form = ApuestasForm(pregunta, request.user, data=request.POST)
        if form.is_valid():
            respuesta_apuesta = form.save(commit=False)
            respuesta_apuesta.user = request.user
            respuesta_apuesta.save()
    context = {
        'pregunta': pregunta,
        'form': form
    }
    return HttpResponse(template.render(context, request))
