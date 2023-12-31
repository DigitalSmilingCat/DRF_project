"""
URL configuration for DRF_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from pereval.views import *
from rest_framework import routers
from .yasg import urlpatterns as yasg_urls
from django.views.static import serve


router = routers.DefaultRouter()
router.register(r'submitData', PerevalViewSet, basename='pereval')
# router.register(r'User', UserViewSet, basename='user')
# router.register(r'Coords', CoordsViewSet, basename='coords')
# router.register(r'Level', LevelViewSet, basename='level')
# router.register(r'Images', ImagesViewSet, basename='images')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]


urlpatterns += yasg_urls