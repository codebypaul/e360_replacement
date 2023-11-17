from django.contrib import admin
from .models import LenderLogin, Loan, EquipPayoff, VehiclePayoff

# Register your models here.
admin.site.register(EquipPayoff)
admin.site.register(VehiclePayoff)
admin.site.register(LenderLogin)
admin.site.register(Loan)