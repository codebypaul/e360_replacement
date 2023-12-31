from django.db import models
# from asset.models import Location
# from customadmin.models import Profile

# Create your models here.

# class Loan(models.Model):
#     loan_statuses = [
#         ('Active','Active'),
#         ('Satisfied','Satisfied')
#     ]
#     contract_id = models.AutoField(primary_key=True)
#     link_to_contract=models.URLField(max_length=300,blank=True,null=True)
#     lender = models.CharField(max_length=40)
#     owned_company = models.CharField(max_length=25)
#     contract_number = models.CharField(max_length=20)
#     start_date = models.DateField(blank=True,null=True)
#     loan_term = models.PositiveSmallIntegerField(blank=True,null=True)
#     interest_rate = models.FloatField(blank=True,null=True)
#     down_payment = models.IntegerField(blank=True,null=True)
#     financed_amount = models.FloatField(blank=True,null=True)
#     monthly_payment = models.FloatField(blank=True,null=True)
#     remaining_payments = models.PositiveSmallIntegerField(blank=True,null=True)
#     loan_status = models.CharField(max_length=20,choices= loan_statuses,blank=True, null=True,default='Active')
#     loan_satisfied_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.lender} - {self.contract_number}'
    
#     class Meta:
#         ordering=['lender','contract_number']

# class Equipment(models.Model):
#     ownership_types = [
#         ('Financed','Financed'),
#         ('Rental','Rental'),
#         ('InterCo','Inter Company Rental'),
#         ('Leased','Leased'),
#         ('Owned','Owned'),
#         ('Sold','Sold'),
#         ('Unknown','Unknown')
#     ]

#     statuses = [
#         ('Active','Active'),
#         ('Inactive','Inactive')
#     ]
#     # companies = [
#     #     ('Nest Homes','Nest Homes'),
#     #     ('Land Crafters','Land Crafters'),
#     #     ('Sidenbury','Sidenbury Holdings'),
#     # ]
#     # id = models.CharField(primary_key=True, unique=True,blank=True,null=True)
#     equipment_id = models.CharField(primary_key=True,max_length=10)
#     status = models.CharField(blank=True,null=True,choices=statuses)
#     serial_number = models.CharField(max_length=30)
#     year = models.PositiveSmallIntegerField(null=True)
#     description = models.CharField(max_length=100)
#     # company_assign = models.CharField(max_length=30, choices=companies)
#     ownership = models.CharField(max_length=20,choices=ownership_types)
#     hours = models.IntegerField()
#     contract = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
#     location = models.ForeignKey(Location,blank=True,null=True,on_delete=models.CASCADE)
#     notes = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.equipment_id
    
#     class Meta:
#         ordering=['equipment_id']

# class Vehicle(models.Model):
#     ownership_types = [
#         ('Financed','Financed'),
#         ('Rental','Rental'),
#         ('InterCo','Inter Company Rental'),
#         ('Leased','Leased'),
#         ('Owned','Owned w/ Title'),
#         ('Newly Owned','Owned w/o Title'),
#         ('Sold','Sold'),
#         ('Unknown','Unknown')
#     ]
#     # companies = [
#     #     ('Nest Homes','Nest Homes'),
#     #     ('Land Crafters','Land Crafters'),
#     #     ('Sidenbury','Sidenbury Holdings'),
#     # ]
#     statuses = [
#         ('Active','Active'),
#         ('Inactive','Inactive')
#     ]
#     # id = models.CharField(primary_key=True, unique =True,blank=True,null=True)
#     equipment_id = models.CharField(primary_key=True,max_length=10)
#     status = models.CharField(blank=True,null=True,choices=statuses)
#     vin = models.CharField(max_length=17,unique=True)
#     year = models.PositiveSmallIntegerField(null=True)
#     description = models.CharField(max_length=100)
#     # company_assign = models.CharField(max_length=30, choices=companies)
#     ownership = models.CharField(max_length=20,choices=ownership_types)
#     mileage = models.IntegerField()
#     contract = models.ForeignKey(Loan,blank=True,null=True,on_delete=models.CASCADE)
#     driver=models.OneToOneField(Profile,on_delete=models.CASCADE,null=True,blank=True)
#     notes = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.equipment_id
    
#     class Meta:
#         ordering=['equipment_id']

# class Note(models.Model):
#     equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
#     resolved = models.BooleanField()
#     note_text = models.TextField()
#     date_created = models.DateField(auto_now=False)
#     date_updated  = models.DateTimeField(auto_now_add=True)