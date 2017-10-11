# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Pregunta, RespuestaValidas


class abm_apuestas(TestCase):

    def setUp(self):
        user = User(username='pdalmasso')
        user.set_password('esta_clave_no_la_uso.')
        user.save()
        pregunta = Pregunta(
            text='¿LLovera?',
            due_date=datetime.now(),
            create_user=user,
            update_user=user,
        )
        pregunta.save()

    def test_crear_pregunta(self):
        user = User.objects.get(username='pdalmasso')
        pregunta = Pregunta(
            text='¿LLovera mañana?',
            due_date=datetime.now(),
            create_user=user,
            update_user=user,
        )
        pregunta.save()

    def test_crear_respuesta_valida(self):
        user = User.objects.get(username='pdalmasso')
        pregunta = Pregunta.objects.get(text='¿LLovera?')
        respuesta = RespuestaValidas(
            pregunta=pregunta,
            text='Si',
            create_user=user,
            update_user=user,
        )
        respuesta.save()

    def test_home(self):
        client = Client()
        response = client.get('/accounts/login/')
        print response.status_code
        print response.context['form']

    def test_login_post_password_error(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username': 'pdalmasso',
                'password': ''
            }
        )
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_login_post_ok(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username': 'pdalmasso',
                'password': 'esta_clave_no_la_uso.'
            }
        )
        validator = True
        if response.status_code == '302':
            validator = False
        validator = False
        self.assertTrue(validator)
