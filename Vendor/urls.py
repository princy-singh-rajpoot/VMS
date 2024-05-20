
from django.urls import path
from .views import create_vendor,list_vendor

urlpatterns = [
    path('vendor/', create_vendor),
    path('vendorslist/', list_vendor),
]
