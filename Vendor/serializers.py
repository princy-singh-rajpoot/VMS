from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False}, 
            'contact_details': {'required': False}, 
            'address': {'required': False}, 
            'on_time_delivery_rate': {'required': False},
            'quality_rating_avg': {'required': False},
            'average_response_time': {'required': False},
            'fulfillment_rate': {'required': False},
            'vendor_code': {'required': False},
        }

