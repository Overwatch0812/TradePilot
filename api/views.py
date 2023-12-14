from django.shortcuts import render
from rest_framework import generics
from .serializers import *
# Create your views here.

class createVendor(generics.CreateAPIView):
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class listVendor(generics.ListAPIView):
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class vendorDetail(generics.RetrieveAPIView):
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()
    lookup_field='pk'

class updateVendorDetail(generics.UpdateAPIView):
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class deleteVendor(generics.DestroyAPIView):
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()