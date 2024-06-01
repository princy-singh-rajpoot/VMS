from django.urls import path
from . import views
from .views import VendorPerformanceAPIView

urlpatterns = [
    path('api/vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/purchase_orders/', views.PurchaseOrderListCreate.as_view()),
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]

