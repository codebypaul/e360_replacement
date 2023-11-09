from django.urls import path
from . import views
from .views import LoanCreate

urlpatterns = [

    # Admin
    path('dashboard/', views.admin_panel,name='admin panel'),
    # Financial
    
    path('new-loan/',LoanCreate.as_view(),name='add new loan'),

]