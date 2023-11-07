from django.urls import path
from . import views

urlpatterns = [
    # Equipment
    path('equipment-dash/',views.equipment_dash,name='equipment dash'),
    
    # Vehicles
    path('vehicle-dash/',views.vehicle_dash,name='vehicle dash'),

]