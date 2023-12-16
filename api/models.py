from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=50)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=50)
    on_time_delivery_rate=models.FloatField(null=True)
    quality_rating_avg=models.FloatField(null=True)
    average_response_time=models.FloatField(null=True)
    fulfillment_rate=models.FloatField(null=True)

class PurchaseOrder(models.Model):
    po_number=models.CharField() #- Unique number identifying the PO.
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE) #- Link to the Vendor model.
    order_date=models.DateTimeField(auto_now=True) #- Date when the order was placed.
    delivery_date=models.DateTimeField(auto_now=True) #- Expected or actual delivery date of the order.
    items=models.JSONField() #- Details of items ordered.
    quantity=models.IntegerField() #- Total quantity of items in the PO.
    status=models.CharField() #- Current status of the PO (e.g., pending, completed, canceled).
    quality_rating=models.FloatField() #- Rating given to the vendor for this PO (nullable).
    issue_date=models.DateTimeField(auto_now=True) #- Timestamp when the PO was issued to the vendor.
    acknowledgment_date=models.DateTimeField(auto_now=True)

class Performance(models.Model):
    vendor= models.ForeignKey(Vendor,on_delete=models.CASCADE)   # - Link to the Vendor model.
    date= models.DateTimeField()   # - Date of the performance record.
    on_time_delivery_rate= models.FloatField()   # - Historical record of the on-time delivery rate.
    quality_rating_avg= models.FloatField()   # - Historical record of the quality rating average.
    average_response_time= models.FloatField()   # - Historical record of the average response time.
    fulfillment_rate= models.FloatField()