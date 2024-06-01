from rest_framework import generics
from .models import Vendor,PurchaseOrder
from .serializers import VendorSerializer, VendorUpdateSerializer,PurchaseOrderSerializer
from .serializers import VendorPerformanceSerializer
from rest_framework.response import Response

# class VendorPerformanceAPIView(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorPerformanceSerializer
#     lookup_url_kwarg = 'vendor_id'
from django.db.models import Avg

def calculate_vendor_performance(vendor):
    # Calculate on-time delivery rate
    on_time_delivery_rate = vendor.historicalperformance_set.aggregate(Avg('on_time_delivery_rate'))['on_time_delivery_rate__avg']
    # Calculate quality rating average
    quality_rating_avg = vendor.historicalperformance_set.aggregate(Avg('quality_rating_avg'))['quality_rating_avg__avg']
    # Calculate average response time
    average_response_time = vendor.historicalperformance_set.aggregate(Avg('average_response_time'))['average_response_time__avg']
    # Calculate fulfillment rate
    fulfillment_rate = vendor.historicalperformance_set.aggregate(Avg('fulfillment_rate'))['fulfillment_rate__avg']

    # Update Vendor model with calculated metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating = quality_rating_avg
    vendor.response_time = average_response_time
    vendor.fulfillment_rate = fulfillment_rate

    # Save the updated vendor instance
    vendor.save()

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        calculate_vendor_performance(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return VendorUpdateSerializer
        return VendorSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
