# -*- coding: utf-8 -*-
from django.apps import apps

from rest_framework import serializers


class ApuestasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        RespuestaValidas = apps.get_model(
            'game', 'RespuestaValidas'
        )
        model = RespuestaValidas
        fields = ('id', 'pregunta_text', 'pregunta_id', 'text')
