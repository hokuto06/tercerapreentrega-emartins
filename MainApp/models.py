from django.db import models

class AccessPoints(models.Model):

    deviceName = models.CharField(max_length=30)
    ipAddress = models.GenericIPAddressField()
    #ipAddress = models.GenericIPAddressField(unique=True) 
    status = models.IntegerField()

class Switches(models.Model):

    deviceName = models.CharField(max_length=30)
    ipAddress = models.GenericIPAddressField(unique=True)
    marca = models.CharField(max_length=30)
    status = models.IntegerField()


