from django.db import models
from department.models import Designation
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, 'MALE'
        FEMALE = 2, 'FEMALE'
        OTHER = 3, 'OTHER'

    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.PositiveBigIntegerField()
    dob = models.DateField()
    gender = models.IntegerField(choices=Gender.choices)
    email = models.EmailField()
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    date_of_join = models.DateField()
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    is_active = models.BooleanField(help_text="Employee status")
    date_of_termination= models.DateField(null=True,blank=True)
    is_lead = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='project_created_by')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='project_modified_by')

    def _str_(self):
        return self.name