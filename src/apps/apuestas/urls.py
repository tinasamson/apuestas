from django.conf.urls import url
from .views import PreguntaView, index
urlpatterns = [
    url(r'^$', index, name='apuestas_index'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view())
]
