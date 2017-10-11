# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
#from django.shortcuts import render
from django.apps import apps

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ApuestasSerializer


class ApuestasViewSet(viewsets.ModelViewSet):
    RespuestaValidas = apps.get_model('game', 'RespuestaValidas')
    queryset = RespuestaValidas.objects.all()
    serializer_class = ApuestasSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['POST'])
def registrar_apuesta(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id', 0)
        respuesta_id = request.POST.get('respuesta_id', 0)
        RespuestaValidas = apps.get_model('game', 'RespuestaValidas')
        Apuestas = apps.get_model('game', 'Apuestas')
        user = User.objects.get(pk=request.user.id)
        respuesta_validas = RespuestaValidas.objects.get(pk=respuesta_id)
        apuesta = Apuestas(
            respuesta_valida=respuesta_validas,
            user=request.user
        )
        apuesta.save()
        return Response({
            'status': 'ok'
        })
    return Response({
        "status": "error",
        "response": ""
    })


"""
method = "POST"
handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)
data = urllib.urlencode([{respuesta_id: '2'}])
request = urllib2.Request(url, data=data)
request.add_header("Content-Type",'application/json')
request.add_header('Authorization', 'token %s' % token)request.add_header('Authorization', 'token %s' % token)
request.get_method = lambda: method
	656c94d31568bf11ed5c0b74d292e850b2ae16c3
try:
    connection = opener.open(request)
except urllib2.HTTPError,e:
    connection = e
if connection.code == 200:
    data = connection.read()
else:
    pass
"""
