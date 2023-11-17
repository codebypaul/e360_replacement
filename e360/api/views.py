# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import EquipmentSerializer, VehicleSerializer #, EmployeeSerializer

# from .models import Equipment, Vehicle #, Employee
# # Create your views here.

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
        
#         'Vehicle List':'/vehicle-list/',
#         'Vehicle Detail View':'vehicle-detail/<str:pk>/',
#         'Create Vehicle':'/vehicle-create/',
#         'Update Vehicle':'/vehicle-update/<str:pk/',
#         'Delete Vehicle':'/vehicle-delete/<str:pk>',
        
#         'Equipment List':'/equipment-list/',
#         'Equipment Detail View':'equipment-detail/<str:pk>/',
#         'Create Equipment':'/equipment-create/',
#         'Update Equipment':'/equipment-update/<str:pk/',
#         'Delete Equipment':'/equipment-delete/<str:pk>',

#         'Employee List':'/employee-list'
#     }
#     return Response(api_urls)
#     # return JsonResponse("API Base Point", safe=False)

# # Equipment

# @api_view(['GET'])
# def equipmentList(request):
#     equipment = Equipment.objects.all()
#     serializer = EquipmentSerializer(equipment, many=True)
#     return Response(serializer.data)

    
    

# @api_view(['GET'])
# def equipmentDetail(request,pk):
#     equipment = Equipment.objects.get(id=pk)
#     serializer = EquipmentSerializer(equipment, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def equipmentCreate(request):
#     serializer = VehicleSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# # Vehicles

# @api_view(['GET'])
# def vehicleList(request):
#     vehicle = Vehicle.objects.all()
#     serializer = VehicleSerializer(vehicle, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def vehicleDetail(request,pk):
#     vehicle = get_object_or_404(Vehicle, id=pk)
#     # vehicle = Vehicle.objects.filter(equipment_id=equipment_id).first()
#     serializer = VehicleSerializer(vehicle, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def vehicleCreate(request):
#     serializer = VehicleSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST']) # untested
# def vehicleUpdate(request,pk):
#     vehicle = Vehicle.objects.filter(id=pk).first()
#     serializer = VehicleSerializer(instance=vehicle, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE']) # untested
# def vehicleDelete(request,pk):
#     vehicle = Vehicle.objects.filter(id=pk).first()
#     vehicle.delete()

#     return Response('Item Successfully Deleted')

# # Employees

# @api_view(['GET'])
# def employeeList(request):
#     employee = Employee.objects.all()
#     serializer = EmployeeSerializer(employee, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def employeeDetail(request,pk):
#     employee = Employee.objects.get(employee_id=pk)
#     serializer = EmployeeSerializer(employee, many=False)
#     return Response(serializer.data)

# @api_view(['POST']) # untested
# def employeeUpdate(request,pk):
#     employee = Employee.objects.filter(employee_id=pk).first()
#     serializer = EmployeeSerializer(instance=employee, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE']) # untested
# def employeeDelete(request,pk):
#     employee = Employee.objects.filter(id=pk).first()
#     employee.delete()

#     return Response('Item Successfully Deleted')