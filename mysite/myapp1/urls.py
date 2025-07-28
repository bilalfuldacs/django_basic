from django.urls import path
from . import views

app_name = 'myapp1'

urlpatterns = [
    # Get all employees
    path('employees/', views.get_all_employees, name='get_all_employees'),
   # path('employees/<int:employee_id>/', views.get_employee_by_id, name='get_employee_by_id'),
    path('departments/', views.get_all_departments, name='get_all_departments'),
] 