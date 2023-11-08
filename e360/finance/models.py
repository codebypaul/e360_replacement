from django.db import models
from api.models import Equipment, Vehicle, Loan

# Create your models here.
class Payoff(models.Model):
    loan=models.ForeignKey(Loan,on_delete=models.CASCADE,null=True,blank=True)
    # equipment=models.ForeignKey(Equipment,on_delete=models.CASCADE,null=True,blank=True)
    # vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True,blank=True)
    payoff=models.FloatField(null=True,blank=True)
    date_acquired=models.DateField(null=True,blank=True)
    valid_thru=models.DateField(null=True,blank=True)

# class Liquidation(models.Model):
#     equipment_id =  models.ForeignKey(Equipment,null=True,on_delete=models.CASCADE)  
#     vehicle_id = models.ForeignKey(Vehicle,db_column='vehicle_id',null=True,on_delete=models.CASCADE) 
#     contract_id = models.ForeignKey(Loan,null=True,on_delete=models.CASCADE)
#     payoff_amount = models.IntegerField
#     as_of_date = models.DateField
#     fair_market_value = models.IntegerField
#     overtime_liq_value = models.IntegerField
#     price_sold = models.IntegerField
#     date_sold = models.DateField