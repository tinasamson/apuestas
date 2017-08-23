# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 21:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apuestas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apuestas.Pregunta')),
            ],
        ),
        migrations.AlterField(
            model_name='respuestavalidas',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_valida_create_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='respuestavalidas',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_valida_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apuestas',
            name='respuesta_valida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuestas.RespuestaValidas'),
        ),
        migrations.AddField(
            model_name='apuestas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='apuestas',
            unique_together=set([('user', 'pregunta')]),
        ),
    ]