"""details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pdb

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from apps.localidade.urls import localidade_api_urls, localidade_urls
from apps.usuario.urls import usuario_api_urls, usuario_urls

api_urls = localidade_api_urls.urls + usuario_api_urls.urls
app_urls = usuario_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('', include('rest_framework.urls')),
    path('', include(api_urls)),
    path('', include(app_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
