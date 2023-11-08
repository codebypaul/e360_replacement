from django.contrib import admin
from .models import Equipment, Vehicle, Loan

# Register your models here.
class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.get_fields()]

class VehicleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vehicle._meta.get_fields()]

class LoanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Loan._meta.get_fields()]
    # ('lender','owned_company','contract_number','start_date')

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Loan)