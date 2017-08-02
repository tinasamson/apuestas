# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pregunta, RespuestasValidas

def add_simbol_text(modeladmin, request, queryset):
    for q in queryset:
        q.text = q.text + '?'
        q.save()
add_simbol_text.short_description = 'Agregar simbolo ?'

class RespuestasValidasHeadInLine(admin.TabularInline):
    model=RespuestasValidas
    extra = 1
    readonly_fields = ('create_user', 'update_user')

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'create_user')
    search_fields = ('text', 'create_user__username')
    list_filter = ('text',)
    inlines = [RespuestasValidasHeadInLine, ]
    actions = [add_simbol_text, ]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(RespuestasValidas)


# Register your models here.
