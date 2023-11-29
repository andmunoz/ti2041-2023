from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('', views.equipment_home, name='characters'),

    path('equipment/', views.equipment_home, name='equipment'),
    path('equipment/weapons', views.weapons_list, name='weapons'),
    path('equipment/weapons/save', views.weapons_save),
    path('equipment/weapons/download', views.weapons_download),
    path('equipment/weapons/upload', views.weapons_upload),
    path('equipment/weapons/refresh', views.weapons_refresh),

    path('', views.equipment_home, name='drugs'),

    path('', views.equipment_home, name='vehicles'),

    path('', views.equipment_home, name='netrunning'),

    path('', views.equipment_home, name='complements'),
]
