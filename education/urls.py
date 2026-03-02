from django.urls import path

from . import views

app_name = 'education'

urlpatterns = [
    path('yonalishlar/', views.directions, name='directions'),
    path('kafedralar/', views.departments_list, name='departments_list'),
    path('oquv-jarayoni/', views.process, name='process'),
    path('baholash/', views.assessment, name='assessment'),
    path('amaliyot/', views.practice, name='practice'),
]