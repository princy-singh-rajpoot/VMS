
from django.urls import path
from .views import create_vendor

urlpatterns = [
    path('vendor/', create_vendor),
]
