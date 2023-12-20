from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',listVendor.as_view()),
    path('vendors/create/',createVendor.as_view()),
    path('vendors/<int:pk>/detail/',vendorDetail.as_view()),
    path('vendors/<int:pk>/update/',updateVendorDetail.as_view()),
    path('vendors/<int:pk>/delete/',deleteVendor.as_view()),
    # For Purchase Order
    path('purchase_order/create/',createPurchaseOrder.as_view()),
    path('purchase_order/<int:pk>/',listPurchaseOrder.as_view()),
    path('purchase_order/<int:pk>/detail/',PurchaseOrderDetail.as_view()),
    path('purchase_order/<int:pk>/update/',updatePurchaseOrderDetail.as_view()),
    path('purchase_order/<int:pk>/delete/',deletePurchaseOrder.as_view()),
    #for performance
    path('vendors/<int:pk>/performance/',PerformanceView.as_view())
]
