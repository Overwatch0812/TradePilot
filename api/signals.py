from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder,Performance,Vendor
from datetime import datetime
from .Calculations import *

# @receiver(post_save,sender=PurchaseOrder)
# def update(sender,instance,created,**kwargs):
#     if not created:
#         print(instance.items)


        
@receiver(post_save,sender=PurchaseOrder)
def after_new_PO(sender,instance,created,**kwargs):
    if not created:
        if instance.status=='completed':
            Vend=Vendor.objects.get(id=instance.vendor.id)
            Vend.on_time_delivery_rate=On_Time_Delivery_Rate(instance.vendor)
            Vend.average_response_time=Average_Response_Time(instance.vendor)
            Vend.fulfillment_rate=Fulfilment_Rate(instance.vendor)
            Vend.save()
            print("no error")
            # print("On_Time_Delivery_Rate:",On_Time_Delivery_Rate(instance.vendor),"%")
            # print("Fulfilment_Rate:",Fulfilment_Rate(instance.vendor),"%")
            # print("Average_Response_Time:",Average_Response_Time(instance.vendor),"%")
            if instance.quality_rating:
                    Vend.quality_rating_avg=Quality_Rating_Average(instance.vendor)
                    Vend.save()
                    print("no error2")
                    # print("Quality_Rating_Average:",Quality_Rating_Average(instance.vendor))    
                    # print("helloo")


# @receiver(post_save,sender=PurchaseOrder)
# def after_update_PO(sender,instance,created,**kwargs):
#     if instance:
#         pass


