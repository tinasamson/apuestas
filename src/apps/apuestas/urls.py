from django.conf.urls import url
from .views import PreguntaView, apuestas_list

urlpatterns = [
    url(r'^$', apuestas_list, name='apuestas_list'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view())
]
