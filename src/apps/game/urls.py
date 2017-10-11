from django.conf.urls import url
from .views import PreguntaView, apuestas_list, apuesta, set_respuesta_api

urlpatterns = [
    url(r'^$', apuestas_list, name='apuestas_list'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view()),
    url(r'^(?P<id_pregunta>\d+)/apuesta/$', apuesta, name='apuesta'),
    url(r'^set_respuesta_api/$', set_respuesta_api),
]
