from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Employee, Department

# Create your views here.

@csrf_exempt
@require_http_methods(["GET"])
def get_all_employees(request):
    """
    View to fetch all employees data
    Returns JSON response with all employee information
    """
    # Get all employees from database
    employees = Employee.objects.all()
    
    # Convert to list of dictionaries
    employees_data = []
    for employee in employees:
        employees_data.append({
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'email': employee.email,
            'phone_number': employee.phone_number,
            'employee_id': employee.employee_id,
            'department_name': employee.department_name,
            'position': employee.position,
            'hire_date': employee.hire_date.strftime('%Y-%m-%d') if employee.hire_date else None,
            'salary': str(employee.salary),
            'is_active': employee.is_active,
            'created_at': employee.created_at.strftime('%Y-%m-%d %H:%M:%S') if employee.created_at else None,
            'updated_at': employee.updated_at.strftime('%Y-%m-%d %H:%M:%S') if employee.updated_at else None,
        })
    
    return JsonResponse({
        'status': 'success',
        'message': f'Found {len(employees_data)} employees',
        'data': employees_data
    })

def get_all_departments(request):
    """
    View to fetch all departments data
    Returns JSON response with all department information
    """
    departments = Department.objects.all()
    departments_data = []
    for department in departments:
        departments_data.append({
            'id': department.id,
            'name': department.name,
            'description': department.description,
            'location': department.location,
            'budget': str(department.budget),
            'is_active': department.is_active,
            'created_at': department.created_at.strftime('%Y-%m-%d %H:%M:%S') if department.created_at else None,
            'updated_at': department.updated_at.strftime('%Y-%m-%d %H:%M:%S') if department.updated_at else None,
        })
    return JsonResponse({
        'status': 'success',
        'message': f'Found {len(departments_data)} departments',
        'data': departments_data
    })