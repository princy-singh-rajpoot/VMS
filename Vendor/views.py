from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer, VendorUpdateSerializer

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return VendorUpdateSerializer
        return VendorSerializer
