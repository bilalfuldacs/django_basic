from django.contrib import admin
from .models import Employee, Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'budget', 'is_active')
    list_filter = ('is_active', 'location')
    search_fields = ('name', 'description', 'location')
    ordering = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'department_name', 'position', 'is_active')
    list_filter = ('department_name', 'is_active', 'hire_date')
    search_fields = ('first_name', 'last_name', 'employee_id', 'email')
    ordering = ('last_name', 'first_name')
