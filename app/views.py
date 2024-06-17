from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
import csv

def insert_business_empoyement_data(self):
    with open('C:\\Users\\Dell\\OneDrive\\Desktop\\django1\\jasmin\\Scripts\\csv_business\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            S=i[0]
            p=i[1]
            d=i[2]
            su=i[3]
            St=i[4]
            u=i[5]
            m=i[6]
            Sub=i[7]
            g=i[8]
            St1=i[9]
            St2=i[10]
            St3=i[11]
            BO=Business_Employeement_Data(Series_reference=S,Period=p,Data_value=d,Suppressed=su,Status=St,Units=u,Magnitude=m,Subject=Sub,Group=g,Series_title_1=St1,Series_title_2=St2,Series_title_3=St3)
            BO.save()
    return HttpResponse('employee data inserted successfully')

