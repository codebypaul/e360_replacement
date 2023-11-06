from django.urls import path, include
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path('',views.home_page, name = 'home page'),
    # Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home page'), name='logout'),
    # Authenticated Views
    path('system-home/', views.system, name='system home page'),
    path('equipment-list/',views.equipment_list, name = 'view all equipment'),
    path('vehicle-list/',views.vehicle_list, name = 'view all vehicles'),

    # Admin Only Pages
    path('admin-panel/',views.admin_panel,name='admin panel'),
    
]