
# -*- coding: utf-8 -*-
from django import forms
from .models import Pregunta, Apuestas


class PreguntaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pregunta
        fields = ('text', 'due_date')
        exclude = ('create_date', 'create_user', 'update_date', 'update_user')
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class': 'form-control'
            }),
            'due_date': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        return super(PreguntaForm, self).save(commit=commit)


class ApuestasForm(forms.ModelForm):

    pregunta = None
    user = None

    def __init__(self, pregunta, user, *args, **kwargs):
        super(ApuestasForm, self).__init__(*args, **kwargs)
        self.pregunta = pregunta
        self.user = user
        self.fields['respuesta_valida'].label = self.pregunta.text
        self.fields['respuesta_valida'].queryset = self.pregunta.respuestas_validas


    class Meta:
        model = Apuestas
        fields = ('respuesta_valida',)
        exclude = ('pregunta', 'date', 'user')
        widgets = {
            'respuesta_valida': forms.Select(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class': 'form-control'
            }),
        }

    def clean_respuesta_valida(self):
        if Apuestas.objects.filter(pregunta=self.pregunta, user=self.user).exists():
            raise forms.ValidationError('Ei sos tonto, ya contestaste esto.')
        else:
	    return self.cleaned_data['respuesta_valida']
