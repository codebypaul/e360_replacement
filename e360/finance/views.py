from django.shortcuts import render
from django.views.generic.detail import DetailView

# Models
from api.models import Loan, Equipment, Vehicle

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin

# Pagination
from django.core.paginator import Paginator

# Create your views here.

# Finance
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

class LoanDetail(LoginRequiredMixin,DetailView):
    model = Loan
    context_object_name = 'loan'
    template_name = 'financial/loan.html'