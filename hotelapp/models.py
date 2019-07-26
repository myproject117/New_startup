from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Manager(models.Model):
     name = models.CharField(max_length=256,blank=False)
     designation = models.CharField(max_length=25,blank=False)

     def __str__(self):
         return self.name



class Customer(models.Model):
     name = models.CharField(max_length=256,blank=False)
     age = models.PositiveIntegerField()
     checkin = models.DateTimeField(auto_now=True,blank=True)
     phoneno = models.PositiveIntegerField()
     idproof = models.ImageField()
     reporting = models.ForeignKey(Manager,on_delete=models.CASCADE)
     Choices = (
         ('Normal','NORMAL'),
         ('Ac','AC'),
         ('Non-ac','NON-AC'),
         ('Delux','DELUX'),
         ('Delux Pro','DELUX PRO'),
         ('Super Delux','SUPER DELUX'),
         ('Suite','SUITE')
    )
     room = models.CharField(max_length=25,choices=Choices,null=True)
     Select = (
         ('net banking','Net banking'),
         ('debit card','Debit Card'),
         ('credit card','Credit Card'),
         ('paytm','PayTm')
     )
     payment_mode = models.CharField(max_length=20,choices=Select,null=True)

     def __str__(self):
         return self.name

     def get_absolute_url(self):
         return reverse('hotelapp:detail',kwargs={'pk':self.pk})
