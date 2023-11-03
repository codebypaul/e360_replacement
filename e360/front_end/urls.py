from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home_page, name = 'home page'),
    path('equipment-list/',views.equipment_list, name = 'view all equipment')
]