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
from django.urls import path, include
from rest_framework import routers

from apps.core.urls import router
from apps.usuario.views import *

usuario_api_urls = router
usuario_api_urls.register('usuario/api', UsuarioViewSet)
usuario_api_urls.register('grupo/api', GroupViewSet)
usuario_api_urls.register('permission/api', PermissionViewSet)

usuario_urls = [
    path('token/api/', ObtainToken.as_view(), name='token_obtain'),
    path('token/check/api/', CheckToken.as_view(), name='token_check'),
    path('token/refresh/api/', RefreshToken.as_view(), name='token_refresh')
]
