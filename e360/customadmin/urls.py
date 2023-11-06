from django.urls import path
from . import views
urlpatterns = [
    # Admin
    path('dashboard/', views.admin_panel,name='admin panel'),
    # Financial
    path('finance-dashboard/', views.financial,name='financial dash'),

    # Asset Management
    path('equipment-dash/',views.equipment,name='equipment dash'),
    path('vehicle-dash/',views.vehicle,name='vehicle dash'),

]