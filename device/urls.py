from django.urls import path

from . import views

urlpatterns = [
    path('list_apis/', views.DevieAPIView.as_view()),
]