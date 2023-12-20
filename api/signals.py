from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder,Performance,Vendor
from datetime import datetime
from .Calculations import *

        
@receiver(post_save,sender=PurchaseOrder)
def after_new_PO(sender,instance,created,**kwargs):
    Vend=Vendor.objects.get(id=instance.vendor.id)
    perform=Performance()
    if not created:
        if instance.status=='completed' and instance.quality_rating:
            Vend.on_time_delivery_rate=On_Time_Delivery_Rate(instance.vendor)
            Vend.average_response_time=Average_Response_Time(instance.vendor)
            Vend.fulfillment_rate=Fulfilment_Rate(instance.vendor)
            Vend.quality_rating_avg=Quality_Rating_Average(instance.vendor)
            Vend.save()
            perform.vendor=instance.vendor
            perform.on_time_delivery_rate= On_Time_Delivery_Rate(instance.vendor)  
            perform.average_response_time=Average_Response_Time(instance.vendor)
            perform.fulfillment_rate=Fulfilment_Rate(instance.vendor)
            perform.quality_rating_avg=Quality_Rating_Average(instance.vendor)
            perform.save()
            print("if")
        else:
            Vend.on_time_delivery_rate=On_Time_Delivery_Rate(instance.vendor)
            Vend.average_response_time=Average_Response_Time(instance.vendor)
            Vend.fulfillment_rate=Fulfilment_Rate(instance.vendor)
            Vend.save()
            perform.vendor=instance.vendor
            perform.on_time_delivery_rate= On_Time_Delivery_Rate(instance.vendor)  
            perform.average_response_time=Average_Response_Time(instance.vendor)
            perform.fulfillment_rate=Fulfilment_Rate(instance.vendor)
            perform.save()
            print("else")



