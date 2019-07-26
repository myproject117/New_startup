from django.contrib import admin
from .models import Manager,Customer

# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name','designation']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','age','checkin','phoneno','idproof','reporting','room','payment_mode']

admin.site.register(Manager,ManagerAdmin)
admin.site.register(Customer,CustomerAdmin)
