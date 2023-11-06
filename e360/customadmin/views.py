from django.shortcuts import render

# models
from api.models import Equipment, Vehicle, Loan

# Pagination
from django.core.paginator import Paginator
# Create your views here.

# Admin only
def admin_panel(request,*args, **kwargs):
    equipment_list = Equipment.objects.all()
    vehicle_list = Vehicle.objects.all()

    #  Pagination
    equip_p = Paginator(Equipment.objects.all(), 10)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)

    vehicle_p = Paginator(Vehicle.objects.all(), 10)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'equipment_list':equipment_list,
        'equipments':equipments,
        'vehicle_list':vehicle_list,
        'vehicles':vehicles
    }
    return render(request,'admin/admin_panel.html',context=context,status=200)

# Finance
def financial(request):
    # Loans
    loan_list=Loan.objects.all()

    loan_p=Paginator(Loan.objects.all(),10)
    loan_page=request.GET.get('l_page')
    loans=loan_p.get_page(loan_page)

    # Equipment w/ loan
    equipment_loan_list=Equipment.objects.exclude(contract_id__isnull=True)

    equip_p = Paginator(Equipment.objects.exclude(contract_id__isnull=True), 10)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)
    # Vehicles w/ loan
    vehicle_loan_list=Vehicle.objects.exclude(contract_id__isnull=True)

    vehicle_p = Paginator(Vehicle.objects.exclude(contract_id__isnull=True), 10)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'loan_list':loan_list,
        'loans':loans,
        'equipment_loan_list':equipment_loan_list,
        'equipments':equipments,
        'vehicle_loan_list':vehicle_loan_list,
        'vehicles':vehicles
    }
    return render(request, 'admin/dashboards/financial.html',context=context,status=200)

# Equipment
def equipment(request):
    equipment_list=Equipment.objects.all()

    equip_p = Paginator(Equipment.objects.all(), 10)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)
    context={
        'equipment_list':equipment_list,
        'equipments':equipments
    }
    return render(request, 'admin/dashboards/equipment.html',context=context,status=200)

# Vehicles
def vehicle(request):
    vehicle_list=Vehicle.objects.all()

    vehicle_p = Paginator(Vehicle.objects.all(), 10)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'vehicle_list':vehicle_list,
        'vehicles':vehicles
    }
    return render(request, 'admin/dashboards/vehicles.html',context=context,status=200)

# Employees
def employees(request):
    vehicle_list=Vehicle.objects.all()

    vehicle_p = Paginator(Vehicle.objects.all(), 10)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'vehicle_list':vehicle_list,
        'vehicles':vehicles
    }
    return render(request, 'admin/dashboards/vehicles.html',context=context,status=200)