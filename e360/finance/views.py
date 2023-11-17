from django.shortcuts import render
from django.views.generic.detail import DetailView
from itertools import chain
# Models
from .models import Loan
from asset.models import Equipment, Vehicle

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Pagination
from django.core.paginator import Paginator

# Create your views here.

# Finance
@login_required()
def financial(request):
    # Loans
    loan_list=Loan.objects.all()
    loan_search_input = request.GET.get('loan_search') or ''
    if loan_search_input:
        loan_p=Paginator(Loan.objects.filter(lender__icontains=loan_search_input),10)
        loan_page=request.GET.get('l_page')
        loans=loan_p.get_page(loan_page)
    else:
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
    return render(request, 'financial/financial_dash.html',context=context,status=200)

# Loan Detail
@login_required()
def loanDetail(request, loan_id):
    loan = Loan.objects.get(pk=loan_id)
    loans = Loan.objects.all()
    equipment=Equipment.objects.filter(contract_id=loan_id)
    vehicles=Vehicle.objects.filter(contract_id=loan_id)    
    print(vehicles)
    context={
        'loan':loan,
        'loans':loans,
        'equipment':equipment,
        'vehicles':vehicles
    }
    return render(request, 'financial/loan.html',context=context,status=200)

@login_required()
def liquidation(request):
    loan_search_input = request.GET.get('loan_search') or ''
    # Have not filtered all loans by search input
    active_loans=Loan.objects.filter(loan_status="Active")

    filtered_loans = Loan.objects.filter(lender__icontains=loan_search_input)
    loan_p=Paginator(filtered_loans,10)
    loan_page=request.GET.get('l_page')
    loans=loan_p.get_page(loan_page)

    vehicles=Vehicle.objects.filter(contract_id__isnull=False)
    equipment=Equipment.objects.filter(contract_id__isnull=False)
    
    equipment_list = list(chain(vehicles,equipment))
    context = {
        'active_loans':active_loans,
        'loans':loans,
        'equipment_list':equipment_list
    }
    return render(request,'financial/liquidation.html',context=context,status=200)