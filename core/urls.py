from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('texnikum-haqida/', views.about, name='about'),
    path('rahbariyat/', views.leadership, name='leadership'),
    path('moddiy-texnik-baza/', views.material_base, name='material_base'),
    path('meyoriy-hujjatlar/', views.documents, name='documents'),
    path("elonlar/", views.announcements_list, name='announcements_list'),
    path("elonlar/<int:pk>/", views.announcement_detail, name='announcement_detail'),
]
