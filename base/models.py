from django.db import models
from django.db.models.base import Model

# Create your models here.


class Customer (models.Model):
    name = models.CharField(max_length=250, null=True)
    surname = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.surname

class Vendor(models.Model):
    name = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=65, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    total = models.IntegerField()
    quantity = models.IntegerField()
    created = models.DateField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    order_number = models.CharField(max_length=250)
    total = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    ordered_by = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    delivery_date = models.DateField()
    ordered_item = models.JSONField()
    sub_total = models.FloatField(null=True)
    vat = models.FloatField(null=True)
    comment = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=250, null=True, choices=STATUS)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_number



class VendorItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    created = models.DateField(auto_now=True)
