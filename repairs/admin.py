from django.contrib import admin

from django.contrib.auth.models import User

from . import models

# Register your models here.


@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone1']
    list_per_page = 10


@admin.register(models.Device)
class Device(admin.ModelAdmin):
    list_display = ['brand', 'model', 'color']


@admin.register(models.RepairOrder)
class RepairOrder(admin.ModelAdmin):
    list_display = ['placed_at', 'customer', 'model']
