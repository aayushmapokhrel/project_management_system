from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee
from client.models import Client

# Create your models here.
class Project(models.Model):
    class Prioritystatus(models.IntegerChoices):
        CRITICAL = 1, "CRITICAL"
        HIGH = 2, "HIGH"
        NORMAL = 3, "NORMAL"
        LOW = 4, "LOW"

    class Projectstatus(models.IntegerChoices):
        ONGOING = 1, "ONGOING"
        COMPLETED = 2, "COMPLETED"
        ONHOLD = 3, "ONHOLD"
        ABORT = 4, "ABORT"

    client = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="project/images", null=True, blank=True)
    # requirements_files = models.FileField(upload_to="", blank=True, null=True)
    priority = models.IntegerField(
        choices=Prioritystatus.choices, default=Prioritystatus.LOW
    )
    description = models.TextField(null=True, blank=True)
    employee = models.ManyToManyField(Employee)
    status = models.IntegerField(choices=Projectstatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="project_modified_field"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="project_created_field"
    )

    def _str_(self):
        return self.name
