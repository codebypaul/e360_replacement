from django.shortcuts import render

from api.models import Equipment, Vehicle
# Create your views here.
def home_page(request):

    return render(request, 'pages/home.html', context = {}, status = 200)