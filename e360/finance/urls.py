from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    
    path('finance-dashboard/', login_required(views.financial),name='finance dash'),
    path('loan/<int:loan_id>',login_required(views.loanDetail), name='loan detail'),

]