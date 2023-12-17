from .models import *

def On_Time_Delivery_Rate(id):
    vendor=PurchaseOrder.objects.filter(vendor=id)
def Quality_Rating_Average(id):
    pass
def Average_Response_Time(id):
    pass
def Fulfilment_Rate(id):
    pass



# On-Time Delivery Rate:
# ● Calculated each time a PO status changes to 'completed'.
# ● Logic: Count the number of completed POs delivered on or before
# delivery_date and divide by the total number of completed POs for that vendor.
#  Quality Rating Average:
# ● Updated upon the completion of each PO where a quality_rating is provided.
# ● Logic: Calculate the average of all quality_rating values for completed POs of
# the vendor.
#  Average Response Time:
# ● Calculated each time a PO is acknowledged by the vendor.
# ● Logic: Compute the time difference between issue_date and
# acknowledgment_date for each PO, and then find the average of these times
# for all POs of the vendor.
#  Fulfilment Rate:Calculated upon any change in PO status.
# ● Logic: Divide the number of successfully fulfilled POs (status 'completed'
# without issues) by the total number of POs issued to the vendor.
