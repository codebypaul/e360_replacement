from django.db import models

# Create your models here.
class Loan(models.Model):
    loan_statuses = [
        ('Active','Active'),
        ('Satisfied','Satisfied')
    ]
    contract_id = models.AutoField(primary_key=True)
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
    loan_status = models.CharField(max_length=20,choices= loan_statuses,blank=True, null=True)
    loan_satisfied_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return f'{self.lender} - {self.contract_number}'

class Equipment(models.Model):
    ownership_types = [
        ('Financed','Financed'),
        ('Rental','Rental'),
        ('InterCo','Inter Company Rental'),
        ('Leased','Leased'),
        ('Owned','Owned'),
        ('Sold','Sold'),
        ('Unknown','Unknown')
    ]

    status = [
        ('Active','Active'),
        ('Retired','Retired')
    ]
    # companies = [
    #     ('Nest Homes','Nest Homes'),
    #     ('Land Crafters','Land Crafters'),
    #     ('Sidenbury','Sidenbury Holdings'),
    # ]
    equipment_id = models.CharField(primary_key=True,max_length=10, unique =True)
    status = models.CharField(blank=True,null=True,choices=status)
    serial_number = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=100)
    # company_assign = models.CharField(max_length=30, choices=companies)
    ownership = models.CharField(max_length=20,choices=ownership_types)
    hours = models.IntegerField()
    contract = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

class Vehicle(models.Model):
    ownership_types = [
        ('Financed','Financed'),
        ('Rental','Rental'),
        ('InterCo','Inter Company Rental'),
        ('Leased','Leased'),
        ('Owned','Owned w/ Title'),
        ('Newly Owned','Owned w/o Title'),
        ('Sold','Sold'),
        ('Unknown','Unknown')
    ]
    # companies = [
    #     ('Nest Homes','Nest Homes'),
    #     ('Land Crafters','Land Crafters'),
    #     ('Sidenbury','Sidenbury Holdings'),
    # ]

    equipment_id = models.CharField(primary_key=True,max_length=10,unique=True)
    vin = models.CharField(max_length=17)
    year = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=100)
    # company_assign = models.CharField(max_length=30, choices=companies)
    ownership = models.CharField(max_length=20,choices=ownership_types)
    mileage = models.IntegerField()
    contract = models.ForeignKey(Loan,blank=True,null=True,on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)



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

class Location(models.Model):
    location_name = models.TextField(blank=True,null=True)

# class Employee(models.Model):
#     employee_id = models.PositiveIntegerField(primary_key=True,unique=True)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     title = models.CharField(max_length=30)
#     active = models.BooleanField(null=True)