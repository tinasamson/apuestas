# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import PreguntaForm
def index(request):
    form = PreguntaForm()
    if request.method == 'POST':
        form = PreguntaForm(data=request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.create_user = request.user
            pregunta.update_user = request.user
            pregunta.save()

    template = loader.get_template('index.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username' : request.user.username,
        'form': form
    }
    return HttpResponse(template.render(context, request))
