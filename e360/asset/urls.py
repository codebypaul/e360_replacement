from django.urls import path
from . import views
from .views import UpdateEquipment, UpdateVehicle

urlpatterns = [
    # Equipment
    path('equipment-dash/',views.equipment_dash,name='equipment dash'),
    path('equipment-update/<str:pk>',UpdateEquipment.as_view(),name='update equipment'),
    
    # Vehicles
    path('vehicle-dash/',views.vehicle_dash,name='vehicle dash'),
    path('vehicle-update/<str:pk>',UpdateVehicle.as_view(),name='update vehicle'),

]