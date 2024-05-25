from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
]

