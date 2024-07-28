from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50, null=True, blank=True)
    client_id = models.CharField(max_length=10, null=True, blank=True)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    website = models.URLField(blank=True)
    address = models.CharField(max_length=50)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='client_created_by')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_modified_by')

    
    def save(self, *args, **kwargs):
        client = Client.objects.count()
        self.client_id = f'Cid-{client}+1'
        super(Client, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name