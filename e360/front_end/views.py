from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

#  Authentication
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# models
from api.models import Equipment, Vehicle

# Pagination
from django.core.paginator import Paginator

# Create your views here.
def home_page(request):

    return render(request, 'pages/home.html', context = {}, status = 200)

# Authentication View
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    fields = '__all__'
    redirect_authenticatwed_user = True

    def get_success_url(self):
        return reverse_lazy('system home page')

# Authenticated User View
def system(request):
    equipment_list = Equipment.objects.all()
    vehicle_list = Vehicle.objects.all()

    #  Pagination
    equip_p = Paginator(Equipment.objects.all(), 10)
    equip_page = request.GET.get('page')
    equipments = equip_p.get_page(equip_page)

    vehicle_p = Paginator(Vehicle.objects.all(), 10)
    vehicle_page = request.GET.get('page')
    vehicles = vehicle_p.get_page(vehicle_page)

    context={
        'equipment_list':equipment_list,
        'equipments':equipments,
        'vehicle_list':vehicle_list,
        'vehicles':vehicles
    }

    return render(request, 'pages/system.html', context = context, status = 200)

def equipment_list(request):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    query_set=Equipment.objects.all()
    equipment_list=[
        {
            "equipment_id":x.equipment_id,
            "status":x.status,
            "serial_number":x.serial_number,
            "year":x.year,
            "description":x.description,
            "ownership":x.ownership,
            "hours":x.hours,
            # "contract":x.contract,
        } for x in query_set
    ]

    data={
        "isUser":False,
        "response":equipment_list
    }

    return JsonResponse(data)

def vehicle_list(request):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    query_set=Equipment.objects.all()
    vehicle_list=[
        {
            "equipment_id":x.equipment_id,
            "status":x.status,
            "vin":x.serial_number,
            "year":x.year,
            "description":x.description,
            "ownership":x.ownership,
            "mileage":x.hours,
            # "contract":x.contract,
        } for x in query_set
    ]

    data={
        "isUser":False,
        "response":vehicle_list
    }

    return JsonResponse(data)

