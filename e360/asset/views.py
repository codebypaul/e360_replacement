from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Equipment,Vehicle
from django.contrib.auth.models import User

# Pagination
from django.core.paginator import Paginator

# Create your views here.

# Equipment
def equipment_dash(request):
    equipment_list=Equipment.objects.all()

    equip_p = Paginator(Equipment.objects.all(), 15)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            # context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

    context={
        'equipment_list':equipment_list,
        'equipments':equipments
    }
    return render(request, 'asset/equipment/equipment_dash.html',context=context,status=200)

class UpdateEquipment(LoginRequiredMixin,UpdateView):
    model=Equipment
    fields= '__all__'
    # context_object_name='equipment'
    template_name = 'asset/equipment/equipment.html'
    success_url = reverse_lazy('equipment dash')


# Vehicles
def vehicle_dash(request):
    search_input=request.GET.get('search-input') or ''

    search_vehicles = Vehicle.objects.filter(equipment_id__icontains=search_input) or Vehicle.objects.filter(description__icontains=search_input) or Vehicle.objects.filter(vin__icontains=search_input)
    vehicle_list=search_vehicles

    vehicle_p = Paginator(search_vehicles, 15)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    
    print(request.GET.get('count_filter'))
    
    context={
        'vehicle_list':vehicle_list,
        'vehicles':vehicles,
    }
    return render(request, 'asset/vehicle/vehicle_dash.html',context=context,status=200)

def updateVehicle(request,equipment_id):
    vehicle=Vehicle.objects.get(equipment_id=equipment_id)
    employees=User.objects.all()
    print(employees)
    context={
        'vehicle':vehicle,
        'employees':employees,
    }
    return render(request,'asset/vehicle/vehicle.html',context=context, status=200)

class UpdateVehicle(LoginRequiredMixin,UpdateView):
    # model=Vehicle
    fields= '__all__'
    # context_object_name='equipment'
    template_name = 'asset/vehicle/vehicle.html'
    success_url = reverse_lazy('vehicle dash')