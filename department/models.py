from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT,related_name='department_created_at')
    modified_by = models.ForeignKey(User, on_delete=models.RESTRICT,related_name='department_modified_at')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,)
    modified_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name
    

class Designation(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="department_field")
    is_active = models.BooleanField()
    created_by =  models.ForeignKey(User, on_delete=models.RESTRICT,related_name='designation_created_at')
    modified_by =  models.ForeignKey(User, on_delete=models.RESTRICT,related_name='designation_modified_at')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def str(self) -> str:
        return self.name