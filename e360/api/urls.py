from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api_overview"),

    # equipment
    path('equipment-list/', views.equipmentList, name='equipment list'),
    path('equipment-detail/<str:equipment_id>/', views.vehicleDetail, name='vehicle detail'),

    # vehicles
    path('vehicle-list/', views.vehicleList, name='vehicle list'),
    path('vehicle-detail/<str:pk>/', views.vehicleDetail, name='vehicle detail'),
    path('vehicle-create/',views.vehicleCreate, name = 'create vehicle'),
    path('vehicle-update/<str:pk>/',views.vehicleUpdate, name = 'update vehicle'),
    path('vehicle-delete/<str:pk>/',views.vehicleDelete, name = 'delete vehicle'),

    # employees
    path('employee-list/', views.employeeList, name='employee list'),
    path('employee-detail/<str:pk>/', views.employeeDetail, name='employee detail'),
    # path('vehicle-create/',views.vehicleCreate, name = 'create vehicle'),
    # path('vehicle-update/<str:pk>/',views.vehicleUpdate, name = 'update vehicle'),
    # path('vehicle-delete/<str:pk>/',views.vehicleDelete, name = 'delete vehicle'),

]