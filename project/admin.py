from django.contrib import admin
from project.models import Project
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','name','price','image','priority','description','deadline','status','modified_by','created_by']
    search_fields=['name']