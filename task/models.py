from django.db import models
from project.models import Project
from employee.models import Employee

class Sprint(models.Model):
    name = models.CharField(max_length=80)
    start_date = models.DateField()
    end_date = models.DateField()
    point = models.PositiveIntegerField()
    created_by = models.ForeignKey(Employee, on_delete=models.RESTRICT, related_name="sprint_created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="sprint_modified_by")

    def str(self):
        return self.name
    




class Task(models.Model):
    class Taskstatus(models.IntegerChoices):
        TODO = 1, 'TODO'
        INPROGRESS = 2, 'INPROGRESS'
        REVIEW = 3, 'REVIEW'
        COMPLETE = 4, 'COMPLETE'
        ONHOLD= 5, 'ONHOLD'
        BACKLOG = 6, 'BACKLOG'
        
    class Tasktype(models.IntegerChoices):
        FEATURES= 1, 'FEATURES'
        BUG = 2, 'BUG'
        TEST = 3, 'TEST'
        QA = 4, 'QA'
        DOCUMENTATION = 5, 'DOCUMENTATION'
        OTHER = 6, 'OTHER'
        
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)             
    name = models.CharField(max_length=200)
    sprint = models.ManyToManyField(Sprint)
    due_date = models.DateField()
    assigned_to = models.ManyToManyField(Employee)
    description = models.TextField(null=True)
    status = models.IntegerField(choices=Taskstatus.choices, default=Taskstatus.TODO)
    type = models.IntegerField(choices=Tasktype.choices, default=Tasktype.FEATURES)
    points = models.IntegerField(default=0)
    created_by = models.ForeignKey(Employee, on_delete=models.RESTRICT, related_name="task_created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="task_modified_by")
    
    def _str_(self):
        return self.name


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    file = models.FileField(upload_to="file", blank=True, null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.RESTRICT,related_name='task_comment_created')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True ,related_name='task_comment_modfied')

    def str(self) -> str:
        return self.comment

