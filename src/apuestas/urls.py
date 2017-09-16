"""apuestas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

from apps.core.views import register_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/', logout, {'next_page': '/'}),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include('apps.api.urls')),
    url(r'^apuestas/', include('apps.game.urls')),
    url(r'^register/', register_user, name = 'register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
