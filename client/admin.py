from django.contrib import admin
from client.models import Client
# Register your models here.

@admin.register(Client)
class Clientadmin(admin.ModelAdmin):
    list_display =['name','client_id','position','email','address','is_active']
    search_fields = ['name']