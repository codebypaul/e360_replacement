from django.contrib import admin
from .models import Equipment, Vehicle, Loan

# Register your models here.


admin.site.register(Equipment)
admin.site.register(Vehicle)
admin.site.register(Loan)