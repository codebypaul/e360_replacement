from django.shortcuts import render
from django.http import JsonResponse

from api.models import Equipment, Vehicle
# Create your views here.
def home_page(request):

    return render(request, 'pages/home.html', context = {}, status = 200)

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