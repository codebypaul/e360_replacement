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