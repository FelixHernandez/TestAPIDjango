from .views import *
from django.urls import path
from . import views
 
 
urlpatterns=[
    path('employees', EmployeesView.as_view()),
    path('employees/<int:id>', EmployeesView.as_view()),
    path('beneficiaries', BeneficiariesView.as_view()),
    path('beneficiaries/<int:id>', BeneficiariesView.as_view())  
]