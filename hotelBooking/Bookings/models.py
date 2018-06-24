from django.db import models
from datetime import datetime


# Create your models here.

#Enum Class to populate the Booking Status of a Hotel
class Status(models.Model):
    STATUS = (
        ('COMPLETED', "COMPLETED"),
        ('DROPPED', "DROPPED"),
    )
    status = models.CharField(max_length=10, choices=STATUS, unique=True)

    def __str__(self):
        return self.status

# Enum for list of features of a particular Hotel
class Feature(models.Model):
    FEATURE = (
        ('SW', "SWIMMING"),
        ('SN', "SNOOKER"),
        ('BAR' , "BAR"),

    )
    feature = models.CharField(max_length=10, choices=FEATURE, unique=True)

    def __str__(self):
        return self.feature

class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.TextField(blank=True, null=True)
    visitorCount = models.IntegerField(blank=True, null=True, default=0)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"


class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    address = models.TextField(blank=True ,null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Booking(models.Model):
    h_id = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    c_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
    amount = models.FloatField(blank=True, null=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    checkInDate = models.DateField(auto_now_add=True,blank=True , null=True)
    checkOutDate = models.DateField(auto_now_add=True,blank=True ,null=True)

    def __str__(self):
        return str(self.h_id)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class HotelFeature(models.Model):
    h_id = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    f_id = models.ForeignKey("Feature", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.f_id)

    class Meta:
        verbose_name = "HotelFeature"
        verbose_name_plural = "HotelFeatures"

class Search(models.Model):
    c_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    checkInDate = models.DateField(blank=True,null=True)
    checkOutDate = models.DateField(blank=True , null=True)
    amount = models.FloatField(blank=True , null=True)

    def __str__(self):
        return str(self.c_id)