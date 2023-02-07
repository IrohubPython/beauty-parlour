from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Branche(models.Model):
    name = models.CharField(max_length=250,null=True,blank=False)
    description = models.TextField(max_length=550,null=True,blank=False)
    image = models.ImageField(upload_to='branche',null=True,blank=False)

class Service(models.Model):
    name = models.CharField(max_length=250,null=True,blank=False)
    branch = models.CharField(max_length=250,null=True, blank=True)
    price = models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=False)
    image = models.ImageField(upload_to='service',null=True,blank=False)
    branchname = models.ForeignKey(Branche,null=True,blank=False,on_delete=CASCADE)

