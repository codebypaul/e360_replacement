from django.urls import path
from . import views
from .views import LoanCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # Admin
    path('dashboard/', views.admin_panel,name='admin panel'),
    # Financial
    
    path('new-loan/',LoanCreate.as_view(),name='add new loan'),
    # Documentation
    path('documentation',login_required(views.documentation), name='documentation')
]