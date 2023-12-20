from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


# For Vendor
class createVendor(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class listVendor(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class vendorDetail(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()
    lookup_field='pk'

class updateVendorDetail(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

class deleteVendor(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VendorSerializer
    queryset=Vendor.objects.all()

# For Purchase Order
class createPurchaseOrder(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class listPurchaseOrder(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
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
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()
    lookup_field='pk'

class updatePurchaseOrderDetail(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class deletePurchaseOrder(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

class PerformanceView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
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
    permission_classes=[IsAuthenticated]
    def get_object(self, pk):
        return PurchaseOrder.objects.get(pk=pk)

    def patch(self, request, pk):
        modelz = self.get_object(pk)
        serializer = PurchaseOrderSerializer(modelz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("wrong parameters")