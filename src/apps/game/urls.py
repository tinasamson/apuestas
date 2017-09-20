from django.conf.urls import url
from .views import PreguntaView, apuestas_list, apuesta

urlpatterns = [
    url(r'^$', apuestas_list, name='apuestas_list'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view()),
    url(r'^(?P<id_pregunta>\d+)/apuesta/$', apuesta, name='apuesta')
    url(r'^(?P<set_respuesta_api>\d+)/apuesta/$', set_respuesta_api)
]
