from .models import *
from datetime import datetime

def On_Time_Delivery_Rate(id):
        in_time=0
        PO=PurchaseOrder.objects.filter(vendor=id)
        for i in PO:
                dateTime1=str(i.expected_delivery_date)
                date1=dateTime1[0:10]
                expected=datetime.strptime(date1,"%Y-%m-%d")
                dateTime2=str(i.delivered_date)
                date2=dateTime2[0:10]
                delivered=datetime.strptime(date2,"%Y-%m-%d")
                if delivered<=expected:
                        in_time+=1
        return (in_time/len(PO))*100

def Quality_Rating_Average(id):
    counter=0
    total=0
    PO=PurchaseOrder.objects.filter(vendor=id)
    for i in PO:
        if i.status=="completed":
            total+=i.quality_rating
            counter+=1
    return total/counter

def Average_Response_Time(id):
    PO=PurchaseOrder.objects.filter(vendor=id)
    total=0
    for i in PO:
        issue_date=str(i.issue_date)
        issue_date1=issue_date[0:10]
        issue_date2=datetime.strptime(issue_date1,"%Y-%m-%d")
        ack=str(i.acknowledgment_date)
        ack1=ack[0:10]
        ack2=datetime.strptime(ack1,"%Y-%m-%d")
        time_diff=(issue_date2-ack2).days
        total+=time_diff
    return total/len(PO)*100



def Fulfilment_Rate(id):
    successful=0
    PO=PurchaseOrder.objects.filter(vendor=id)
    for i in PO:
        if i.status=="completed":
            successful+=1
    return successful/len(PO)*100


