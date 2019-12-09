from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

api_name = 'api'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'devices', views.DeviceListViewSet)


urlpatterns = [
    url(r'devices/:<id>', views.DeviceDetailViewSet.as_view(), name='devices')
]
urlpatterns = urlpatterns + router.urls

"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'devices/', views.DeviceListView.as_view(), name="device-all"),
    url(r'users/', views.UserViewSet.as_view({'get':'list'}), name="users"),
    url(r'groups/', views.GroupViewSet.as_view({'get':'list'}), name="groups"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
"""
