from django.urls import path
from . import views
from .views import LoanDetail


urlpatterns=[
    
    path('finance-dashboard/', views.financial,name='finance dash'),
    path('loan/<int:pk>',LoanDetail.as_view(), name='loan detail'),

]