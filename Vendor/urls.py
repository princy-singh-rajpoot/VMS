
from django.urls import path
from .views import create_vendor,list_vendor,specific_vendor
from . import views

urlpatterns = [
    path('vendor/', create_vendor),
    path('vendorslist/', list_vendor),
    path('vendor/<int:vendor_id>/', specific_vendor),
]
