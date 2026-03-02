from django.urls import path

from . import views

app_name = 'youth'

urlpatterns = [
    path('', views.index, name='index'),
]