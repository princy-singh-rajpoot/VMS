from django.shortcuts import render
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse,Http404

def specific_vendor(request,vendor_id):
   try:
        vendor = Vendor.objects.get(id=vendor_id)
        vendor_data = {
            'id': vendor.id,
            'name': vendor.name,
            'contact_details': vendor.contact_details,
            'address': vendor.address,
            'vendor_code':vendor.vendor_code,
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return JsonResponse(vendor_data)
   except Vendor.DoesNotExist:
    raise Http404("Vendor does not exist")

def list_vendor(request):
    vendors = Vendor.objects.all().values()
    vendor_list = list(vendors)  
    return JsonResponse(vendor_list, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_vendor(request):
    name = request.data['name']
    contact_details = request.data['contact_details']
    vendor_code = request.data['vendor_code']
    on_time_delivery_rate = request.data['on_time_delivery_rate']
    quality_rating_avg = request.data['quality_rating_avg']
    average_response_time = request.data['average_response_time']
    fulfillment_rate = request.data['fulfillment_rate']
    
    new_vendor = Vendor(
        name=name,
        contact_details=contact_details,
        vendor_code=vendor_code,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time, 
        fulfillment_rate=fulfillment_rate
        )
    new_vendor.save()
    
    return JsonResponse({'message': 'Data received successfully'}, status=200)
    
    
