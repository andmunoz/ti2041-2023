from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<post_id>/', views.index),
    path('category/<category_id>/', views.index),
    path('hashtag/<hashtag_id>/', views.index),
]
