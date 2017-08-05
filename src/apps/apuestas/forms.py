# -*- coding: utf-8 -*-

from django import forms
from .models import Pregunta, RespuestasValidas


class PreguntaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pregunta
        fields = ('text', 'due_date')
        exclude = ('create_date', 'create_user', 'update_date', 'update_user')

        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder' : 'Ingrese la pregunta.'

                }),
        }
    def save(self, commit=True):
        return super(PreguntaForm, self).save(commit=commit)
