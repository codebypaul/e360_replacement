from django.contrib import admin
from .models import  EquipPayoff, VehiclePayoff, LenderLogin

# Register your models here.
admin.site.register(EquipPayoff)
admin.site.register(VehiclePayoff)
admin.site.register(LenderLogin)