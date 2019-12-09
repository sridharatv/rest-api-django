from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('dev_view', views.DeviceVeiwSet, base_name='dev_view')

urlpatterns = [
    path('list_apis/', views.DevieAPIView.as_view()),
    path('', include(router.urls))
]

