from django.db import models
from adminapp.models import Service
from django.db.models.deletion import CASCADE

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=255,blank=False,null=True)
    email = models.EmailField(blank=False,null=True)
    mobile = models.IntegerField(blank=False,null=True)
    password1 = models.CharField(max_length=255,blank=False,null=True)
    password2 = models.CharField(max_length=255,blank=False,null=True)

class Cart(models.Model):
    serviceid = models.ForeignKey(Service,on_delete=CASCADE,null=True,blank=True)
    userid = models.ForeignKey(Register,on_delete=CASCADE,null=True,blank=False)
    total = models.IntegerField(null=True,blank=False)
    status = models.IntegerField(null=True,blank=False)

class Checkout(models.Model):
    userid = models.ForeignKey(Register,on_delete=CASCADE,null=True,blank=False)
    cartid = models.ForeignKey(Cart,on_delete=CASCADE,null=True,blank=False)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    fname = models.CharField(max_length=255,blank=False,null=True)
    lname = models.CharField(max_length=255,blank=False,null=True)
    email = models.EmailField(blank=False,null=True)
    mobile = models.IntegerField(blank=False,null=True)


class Contact(models.Model):
    name = models.CharField(max_length=255,blank=False,null=True)
    email = models.EmailField(blank=False,null=True)
    conatct = models.IntegerField(blank=False,null=True)
    subject = models.CharField(max_length=255,blank=False,null=True)
    message = models.TextField(max_length=550,null=True,blank=False)

















