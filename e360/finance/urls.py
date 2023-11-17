from django.urls import path
from . import views


urlpatterns=[
    
    path('finance-dashboard/', views.financial,name='finance dash'),
    path('loan/<int:loan_id>',views.loanDetail, name='loan detail'),
    path('liquidation/',views.liquidation,name='liquidation')

]