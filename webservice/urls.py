"""webservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, re_path
from rest_framework import routers

#from api import views
#from device import views as dev_view

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile_api.urls')),
#    path('', include('device.urls')),
#    url(r'', include('api.urls')),
]

""" 
url(r'', include('api.urls')),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^$', views.index, name='index'),
re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
url(r'^$', views.index, name='index'),
url(r'devices/', views.DeviceListView.as_view(), name="device-all"),
"""