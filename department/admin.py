from django.contrib import admin

from department.models import Designation, Department


# Register your models here.
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "department",
        "is_active",
        "created_by",
        "modified_by",
        "created_at",
        "modified_at",
    ]
    # list_display= [f.name for f in Designation._meta.get_fields()]
    search_fields = ["id", "name"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_by", "created_at"]
    search_fields = ["name"]
