from django.http import HttpResponse
from django.shortcuts import render
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes([AllowAny])
def create_vendor(request):
    name = request.data['name']
    vendor_code = request.data['vendor_code']
    on_time_delivery_rate = request.data['on_time_delivery_rate']
    quality_rating_avg = request.data['quality_rating_avg']
    average_response_time = request.data['average_response_time']
    fulfillment_rate = request.data['fulfillment_rate']
    
    new_vendor = Vendor(
        name=name,
        vendor_code=vendor_code,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time, 
        fulfillment_rate=fulfillment_rate
        )
    new_vendor.save()
    
    return JsonResponse({'message': 'Data received successfully'}, status=200)
    