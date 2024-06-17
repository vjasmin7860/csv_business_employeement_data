from django.db import models

# Create your models here.
class Business_Employeement_Data(models.Model):
    Series_reference=models.CharField(max_length=100)
    Period=models.DecimalField(max_digits=10,decimal_places=2)
    Data_value=models.IntegerField(null=True,blank=True)
    Suppressed=models.CharField(max_length=100,null=True,blank=True)
    Status=models.CharField(max_length=100)
    Units=models.CharField(max_length=100)
    Magnitude=models.IntegerField()
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    Series_title_2=models.CharField(max_length=100)
    Series_title_3=models.CharField(max_length=100)