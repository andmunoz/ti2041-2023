from django.urls import path
from .api import api

urlpatterns = [
    path('v1/', api.urls),
]
