from django.contrib import admin
from employee.models import Employee

# Register your models here.


@admin.register(Employee)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "address",
        "phone",
        "email",
        "employee_id",
        "designation",
        "date_of_join",
        "designation",
    ]
    search_fields = ["designation"]
