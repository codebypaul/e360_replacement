from django.db import models
from asset.models import Equipment

# Create your models here.
class Loan(models.Model):
    loan_statuses = [
        ('Active','Active'),
        ('Satisfied','Satisfied')
    ]
    contract_id = models.AutoField(primary_key=True)
    link_to_contract=models.URLField(max_length=300,blank=True,null=True)
    lender = models.CharField(max_length=40)
    owned_company = models.CharField(max_length=25)
    contract_number = models.CharField(max_length=20)
    start_date = models.DateField(blank=True,null=True)
    loan_term = models.PositiveSmallIntegerField(blank=True,null=True)
    interest_rate = models.FloatField(blank=True,null=True)
    down_payment = models.IntegerField(blank=True,null=True)
    financed_amount = models.FloatField(blank=True,null=True)
    monthly_payment = models.FloatField(blank=True,null=True)
    remaining_payments = models.PositiveSmallIntegerField(blank=True,null=True)
    loan_status = models.CharField(max_length=20,choices= loan_statuses,blank=True, null=True,default='Active')
    loan_satisfied_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.lender} - {self.contract_number}'
    
    class Meta:
        ordering=['lender','contract_number']

class EquipPayoff(models.Model):
    # equipment =  models.OneToOneField(Equipment,null=True,on_delete=models.CASCADE)  
    payoff_amount = models.FloatField(null=True,blank=True)
    as_of_date = models.DateField(null=True,blank=True)
    fair_market_value = models.IntegerField(null=True,blank=True)
    # overtime_liq_value = models.IntegerField
    # price_sold = models.IntegerField
    # date_sold = models.DateField

    # def __str__(self):
    #     return self.equipment.equipment_id
    
    # class Meta:
    #     ordering =['equipment']

class VehiclePayoff(models.Model):  
    # vehicle = models.OneToOneField(Vehicle,db_column='vehicle_id',null=True,on_delete=models.CASCADE) 
    payoff_amount = models.FloatField(null=True,blank=True)
    as_of_date = models.DateField(null=True,blank=True)
    fair_market_value = models.IntegerField(null=True,blank=True)

    # def __str__(self):
    #     return self.vehicle.equipment_id
    
    # class Meta:
    #     ordering =['vehicle']
        
class LenderLogin(models.Model):
    lender=models.CharField(null=True,blank=True)
    website=models.URLField(null=True,blank=True)
    username=models.CharField(null=True,blank=True)
    password=models.CharField(null=True,blank=True)
    customer_serv_num=models.CharField(max_length=10,null=True,blank=True)
    mfa_num=models.CharField(max_length=10,null=True,blank=True)
    security_one=models.CharField(null=True,blank=True)
    answer_one=models.CharField(null=True,blank=True)
    security_two=models.CharField(null=True,blank=True)
    answer_two=models.CharField(null=True,blank=True)
    security_three=models.CharField(null=True,blank=True)
    answer_three=models.CharField(null=True,blank=True)

    def __str__(self):
        return f'{self.lender} - {self.username}'
    
    class Meta:
        ordering=['lender']
    