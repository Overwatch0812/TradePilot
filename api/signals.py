from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder,Performance,Vendor

# @receiver(post_save,sender=PurchaseOrder)
# def update(sender,instance,created,**kwargs):
#     if not created:
#         print(instance.items)
def On_Time_Delivery_Rate(id):
        vendor=PurchaseOrder.objects.filter(vendor=id)

        # for i in vendor:
        #     if i.delivery_date == :
        #         arr.append(i)
        # for i in vendor:
        #     if i.status == 'completed':
        #         arr.append(i)
        print(len(vendor))

        
@receiver(post_save,sender=PurchaseOrder)
def after_new_PO(sender,instance,created,**kwargs):
    if instance.vendor:
        On_Time_Delivery_Rate(instance.vendor)

# @receiver(post_save,sender=PurchaseOrder)
# def after_update_PO(sender,instance,created,**kwargs):
#     if instance:
#         pass


