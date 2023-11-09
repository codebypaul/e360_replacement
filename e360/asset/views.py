from django.shortcuts import render
# Models
from api.models import Equipment,Vehicle
# Pagination
from django.core.paginator import Paginator

# Create your views here.

# Equipment
def equipment_dash(request):
    equipment_list=Equipment.objects.all()

    equip_p = Paginator(Equipment.objects.all(), 15)
    equip_page = request.GET.get('e_page')
    equipments = equip_p.get_page(equip_page)

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks']=context['tasks'].filter(user=self.request.user)
    #     context['count']=context['tasks'].filter(complete=False)

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['tasks'] = context['tasks'].filter(title__icontains=search_input)
    #         # context['tasks'] = context['tasks'].filter(title__startswith=search_input)

    #     context['search_input'] = search_input
    #     return context

    context={
        'equipment_list':equipment_list,
        'equipments':equipments
    }
    return render(request, 'asset/equipment.html',context=context,status=200)

# Vehicles
def vehicle_dash(request):
    vehicle_list=Vehicle.objects.all()

    vehicle_p = Paginator(Vehicle.objects.all(), 15)
    vehicle_page = request.GET.get('v_page')
    vehicles = vehicle_p.get_page(vehicle_page)

    # print(request.GET.get('count_filter'))
    context={
        'vehicle_list':vehicle_list,
        'vehicles':vehicles
    }
    return render(request, 'asset/vehicles.html',context=context,status=200)