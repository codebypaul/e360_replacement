from django.db import models
from customadmin.models import Profile
from finance.models import Loan

# Create your models here.
class Location(models.Model):
    location_name = models.TextField(blank=True,null=True)
    active_jobsite=models.BooleanField(default=False)

    def __str__(self):
        return self.location_name
    
    class Meta:
        ordering = ['location_name']

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

    statuses = [
        ('Active','Active'),
        ('Inactive','Inactive')
    ]
    # companies = [
    #     ('Nest Homes','Nest Homes'),
    #     ('Land Crafters','Land Crafters'),
    #     ('Sidenbury','Sidenbury Holdings'),
    # ]
    equipment_id = models.CharField(primary_key=True,max_length=10)
    status = models.CharField(blank=True,null=True,choices=statuses)
    serial_number = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=100)
    ownership = models.CharField(max_length=20,choices=ownership_types)
    hours = models.IntegerField()
    contract = models.ForeignKey(Loan, blank=True, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,blank=True,null=True,on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.equipment_id
    
    class Meta:
        ordering=['equipment_id']

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
    statuses = [
        ('Active','Active'),
        ('Inactive','Inactive')
    ]
    equipment_id = models.CharField(primary_key=True,max_length=10)
    status = models.CharField(blank=True,null=True,choices=statuses)
    vin = models.CharField(max_length=17,unique=True)
    year = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=100)
    ownership = models.CharField(max_length=20,choices=ownership_types)
    mileage = models.IntegerField()
    contract = models.ForeignKey(Loan,blank=True,null=True,on_delete=models.CASCADE)
    driver=models.OneToOneField(Profile,on_delete=models.CASCADE,null=True,blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.equipment_id
    
    class Meta:
        ordering=['equipment_id']