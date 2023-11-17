from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# models
from asset.models import Equipment, Vehicle
from finance.models import Loan
from django.contrib.auth.models import User

# Pagination
from django.core.paginator import Paginator
# Create your views here.

# Admin only
@login_required()
def admin_panel(request,*args, **kwargs):
    # Employees
    employee_search=request.GET.get('employee-search') or ''
    employee_lookup = User.objects.filter(first_name__icontains=employee_search) or User.objects.filter(last_name__icontains=employee_search)
    employee_list=employee_lookup.order_by('last_name')   

    employ_p = Paginator(employee_list, 15)
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

class LoanCreate(LoginRequiredMixin,CreateView):
    model = Loan
    fields = ['lender','owned_company','contract_number','start_date','loan_term','interest_rate','down_payment','financed_amount','monthly_payment']
    success_url = reverse_lazy('financial dash')
    template_name = 'financial/loan_form.html'
    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(LoanCreate, self).form_valid(form)


# Employees
@login_required()
def employees(request):
    # vehicle_list=Vehicle.objects.all()

    # vehicle_p = Paginator(Vehicle.objects.all(), 10)
    # vehicle_page = request.GET.get('v_page')
    # vehicles = vehicle_p.get_page(vehicle_page)

    context={
        # 'vehicle_list':vehicle_list,
        # 'vehicles':vehicles
    }
    return render(request, 'admin/dashboards/vehicles.html',context=context,status=200)

# Documentation
@login_required()
def documentation(request):
    return render(request,'admin/documentation.html')