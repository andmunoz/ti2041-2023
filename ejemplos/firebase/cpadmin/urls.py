from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipment/', views.equipment_home, name='equipment'),
    path('equipment/weapons', views.weapons_list, name='weapons'),
]
