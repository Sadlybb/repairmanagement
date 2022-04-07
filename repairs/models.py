
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    national_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone1 = models.CharField(max_length=11)
    phone2 = models.CharField(max_length=11, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    INTERNAL_STORAGE_CHOICES = [
        ('8gb', '8GB'),
        ('16gb', '16GB'),
        ('32gb', '32GB'),
        ('64gb', '64GB'),
        ('128gb', '128GB'),
        ('256gb', '256GB'),
        ('512gb', '512GB'),
        ('1tb', '1TB'),
        ('2tb', '2TB'),
    ]

    serial_number = models.CharField(max_length=40, primary_key=True)
    imei1 = models.CharField(max_length=15, null=True, blank=True)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    inernal_storage = models.CharField(
        max_length=5, choices=INTERNAL_STORAGE_CHOICES)
    imei2 = models.CharField(max_length=15, null=True, blank=True)


class RepairOrder(models.Model):
    PROBLEM_CATEGORY_CHOICES = [
        ('battery', 'Battery Problem'),
        ('lcd', 'LCD Problem'),
        ('audio', 'Audio Problem'),
        ('water', 'Water Damaged'),
        ('dead', 'Dead'),
    ]
    device_problem_category = models.CharField(
        max_length=255, choices=PROBLEM_CATEGORY_CHOICES)
    device_was_repaired = models.BooleanField(default=False)
    device_is_waterdamaged = models.BooleanField(default=False)
    device_condition = models.TextField()
    placed_at = models.DateTimeField(auto_now_add=True)
    final_cost = models.IntegerField()
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name='orders')
    device = models.ForeignKey(
        Device, on_delete=models.PROTECT, related_name='orders')
    employee = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='orders')


class OrderDetail(models.Model):
    order_id = models.OneToOneField(
        RepairOrder, on_delete=models.PROTECT, related_name='details')
    status = models.CharField(max_length=10)
    estimated_date_of_complition = models.DateField()
    estimated_cost = models.IntegerField()
    status_update_at = models.DateTimeField(auto_now=True)
