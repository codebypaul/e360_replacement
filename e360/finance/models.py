from django.db import models
from api.models import Equipment, Vehicle, Loan

# Create your models here.
class Payoff(models.Model):
    loan=models.ForeignKey(Loan,on_delete=models.CASCADE)
    equipment=models.ForeignKey(Equipment,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    payoff=models.FloatField()
    date_acquired=models.DateField()
    dvalid_thru=models.DateField()