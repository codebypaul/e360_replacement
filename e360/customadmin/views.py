from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
# models
from api.models import Equipment, Vehicle, Loan
from django.contrib.auth.models import User

# Pagination
from django.core.paginator import Paginator
# Create your views here.

# Admin only
def admin_panel(request,*args, **kwargs):
    # Employees
    employee_list=User.objects.all()    

    employ_p = Paginator(User.objects.all(), 15)
    employ_page = request.GET.get('emp_page')
    employees = employ_p.get_page(employ_page)
    #  Equipment
    equipment_list = Equipment.objects.all()

    equip_p = Paginator(Equipment.objects.all(), 15)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)

    # Vehicles
    vehicle_list = Vehicle.objects.all()

    vehicle_p = Paginator(Vehicle.objects.all(), 15)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'employee_list':employee_list,
        'employees':employees,
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

class LoanCreate(LoginRequiredMixin,CreateView):
    model = Loan
    fields = ['lender','owned_company','contract_number','start_date','loan_term','interest_rate','down_payment','financed_amount','monthly_payment']
    success_url = reverse_lazy('financial dash')
    template_name = 'financial/loan_form.html'
    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(LoanCreate, self).form_valid(form)



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