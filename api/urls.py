from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',listVendor.as_view()),
    path('vendors/create/',createVendor.as_view()),
    path('vendors/<int:pk>/detail/',vendorDetail.as_view()),
    path('vendors/<int:pk>/update/',updateVendorDetail.as_view()),
    path('vendors/<int:pk>/delete/',deleteVendor.as_view()),
]
