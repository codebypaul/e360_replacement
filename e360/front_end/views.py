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

# 
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
    return render(request, 'pages/system.html', context = {}, status = 200)

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

# Admin only
def admin_panel(request,*args, **kwargs):
    equipments = Equipment.objects.all()
    vehicles = Vehicle.objects.all()
    context={
        'equipments':equipments,
        'vehicles':vehicles
    }
    return render(request,'admin/admin_panel.html',context=context,status=200)