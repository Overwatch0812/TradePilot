from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse
from .models import *
# Create your views here.


# For Vendor
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

# For Purchase Order
class createPurchaseOrder(generics.CreateAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class listPurchaseOrder(generics.ListAPIView):
    def get_queryset(self):
        queryset=PurchaseOrder.objects.all()
        return queryset
    def get(self,request,pk):
        orders=PurchaseOrder.objects.filter(vendor=pk)
        if orders:
            serialized=PurchaseOrderSerializer(orders,many=True)
            return Response(serialized.data)
        else:
            return HttpResponse("No Orders of current vendor")

class PurchaseOrderDetail(generics.RetrieveAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()
    lookup_field='pk'

class updatePurchaseOrderDetail(generics.UpdateAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class deletePurchaseOrder(generics.DestroyAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class PerformanceView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset=Performance.objects.all()
        return queryset
    def get(self,request,pk):
        perform=Performance.objects.filter(vendor=pk).latest('date')
        if perform:
            serialized=PerformanceSerializer(perform)
            return Response(serialized.data)
        else:
            return HttpResponse("No Orders of current vendor")
    

class Recalc(APIView):
    def get_object(self, pk):
        return PurchaseOrder.objects.get(pk=pk)

    def patch(self, request, pk):
        modelz = self.get_object(pk)
        serializer = PurchaseOrderSerializer(modelz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")